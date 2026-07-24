import os
import sys
import json
import glob
import re

try:
    import yaml
except ImportError:
    print("El paquete 'pyyaml' no está instalado. Instalándolo o ejecutando sin él...")
    os.system("pip install pyyaml")
    import yaml

def extract_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content
    
    yaml_text = match.group(1)
    body_text = match.group(2)
    try:
        metadata = yaml.safe_load(yaml_text)
        return metadata, body_text
    except Exception as e:
        print(f"Error parseando YAML en {file_path}: {e}")
        return None, content

def validate_repository(repo_dir):
    schema_path = os.path.join(repo_dir, "schema", "norm_schema.json")
    if os.path.exists(schema_path):
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        allowed_categories = schema["properties"]["clasificacion"]["properties"]["categoria_canonica"]["enum"]
    else:
        allowed_categories = [
            "01_marco_normativo_general_y_organico",
            "02_gestion_y_administracion_centros",
            "03_ordenacion_curricular_y_ensenanzas",
            "04_organizacion_escolar_y_funcionamiento",
            "05_alumnado_y_servicios_escolares",
            "06_atencion_diversidad_y_orientacion",
            "07_convivencia_bienestar_y_protocolos",
            "08_personal_docente",
            "09_personal_laboral_y_no_docente"
        ]

    md_files = glob.glob(os.path.join(repo_dir, "**", "*.md"), recursive=True)
    
    ids_seen = {}
    errors = 0
    valid_count = 0

    for md_file in md_files:
        filename = os.path.basename(md_file)
        if filename in ["README.md", "LICENSE.md", "walkthrough.md", "implementation_plan.md"]:
            continue

        rel_path = os.path.relpath(md_file, repo_dir)
        metadata, _ = extract_frontmatter(md_file)

        if not metadata:
            print(f"[ERROR: SIN FRONTMATTER] {rel_path}")
            errors += 1
            continue

        # Check required fields
        norm_id = metadata.get("id")
        if not norm_id:
            print(f"[ERROR: ID FALTANTE] {rel_path}")
            errors += 1
        elif norm_id in ids_seen:
            print(f"[ERROR: ID DUPLICADO] '{norm_id}' en {rel_path} (ya visto en {ids_seen[norm_id]})")
            errors += 1
        else:
            ids_seen[norm_id] = rel_path

        # Check canonical category matching path
        clasif = metadata.get("clasificacion", {})
        cat = clasif.get("categoria_canonica")
        if not cat or cat not in allowed_categories:
            print(f"[ERROR: CATEGORIA INVALIDA] '{cat}' en {rel_path}")
            errors += 1
        elif cat not in rel_path.replace("\\", "/"):
            print(f"[AVISO: DESALINEACION CARPETA-CATEGORIA] {rel_path} dice categoria '{cat}'")

        valid_count += 1

    print("\n" + "="*50)
    print(f"Resultados de Validación OKF:")
    print(f" - Documentos normativos procesados: {valid_count}")
    print(f" - Identificadores únicos: {len(ids_seen)}")
    print(f" - Errores detectados: {errors}")
    print("="*50)

    return errors == 0

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    success = validate_repository(repo_root)
    sys.exit(0 if success else 1)
