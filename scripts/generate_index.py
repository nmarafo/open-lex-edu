import os
import sys
import glob
import re
import json

try:
    import yaml
except ImportError:
    os.system("pip install pyyaml")
    import yaml

def extract_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return None
    
    yaml_text = match.group(1)
    try:
        return yaml.safe_load(yaml_text)
    except Exception as e:
        print(f"Error cargando YAML en {file_path}: {e}")
        return None

def build_index(repo_dir):
    md_files = glob.glob(os.path.join(repo_dir, "**", "*.md"), recursive=True)
    
    nodes = {}
    graph = []

    for md_file in md_files:
        filename = os.path.basename(md_file)
        if filename in ["README.md", "LICENSE.md", "walkthrough.md", "implementation_plan.md"]:
            continue

        rel_path = os.path.relpath(md_file, repo_dir).replace("\\", "/")
        metadata = extract_frontmatter(md_file)

        if not metadata or "id" not in metadata:
            continue

        norm_id = metadata["id"]
        nodes[norm_id] = {
            "id": norm_id,
            "codigo_sintetizado": metadata.get("codigo_sintetizado", ""),
            "titulo": metadata.get("titulo", ""),
            "jurisdiccion": metadata.get("jurisdiccion", ""),
            "ambito": metadata.get("ambito", ""),
            "tipo_disposicion": metadata.get("tipo_disposicion", ""),
            "fecha_publicacion": metadata.get("fecha_publicacion", ""),
            "estado": metadata.get("estado", "Vigente"),
            "redaccion": metadata.get("redaccion", "original"),
            "categoria_canonica": metadata.get("clasificacion", {}).get("categoria_canonica", ""),
            "subcategoria": metadata.get("clasificacion", {}).get("subcategoria", ""),
            "tags": metadata.get("tags", []),
            "path": rel_path
        }

        # Collect relationships
        relaciones = metadata.get("relaciones", {})
        for rel_type, items in relaciones.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict) and "norma_id" in item:
                        graph.append({
                            "origen": norm_id,
                            "tipo": rel_type,
                            "destino": item["norma_id"],
                            "articulos_origen": item.get("articulos_origen", []),
                            "articulos_destino": item.get("articulos_destino", [])
                        })

    index_data = {
        "version": "1.0",
        "total_normas": len(nodes),
        "normas": nodes,
        "relaciones_grafo": graph
    }

    index_path = os.path.join(repo_dir, "index.yaml")
    with open(index_path, 'w', encoding='utf-8') as f:
        yaml.dump(index_data, f, allow_unicode=True, sort_keys=False)

    print(f"[OK] 'index.yaml' generado con exito ({len(nodes)} normas y {len(graph)} relaciones).")

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    build_index(repo_root)
