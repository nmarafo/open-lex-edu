# 📚 open-lex-edu (Open Knowledge Format - Normativa Educativa)

Base de conocimiento estructurada basada en la especificación **Open Knowledge Format (OKF)** para la gestión, consulta y procesamiento por Inteligencia Artificial y agentes de la legislación educativa en España (**Estatal** y **Autonómica: Canarias**).

---

<!-- AI_AGENT_INSTRUCTIONS_START -->
> [!NOTE]
> **INSTRUCTIONS FOR AI AGENTS & LLMs**
> 
> This repository is formatted using the Open Knowledge Format (OKF).
> 1. **Index First:** Do NOT scan all files if searching for a specific topic. Read `index.yaml` first to identify the relevant file paths and metadata.
> 2. **Metadata Headers:** Every document contains a YAML frontmatter with legal scope (`jurisdiccion`, `ambito`), publication dates, status (`estado`), and consolidation type (`redaccion`).
> 3. **Canonical Sources:** Always prioritize documents marked with `estado: "Vigente"`.
<!-- AI_AGENT_INSTRUCTIONS_END -->

---

## 🎯 Objetivo

El propósito de este repositorio es ofrecer la normativa jurídica de educación de forma **estructurada, versionada y en texto plano (Markdown)**. Esto permite:
* **Para personas:** Consultar leyes, reales decretos, decretos y órdenes sin la sobrecarga sintáctica de documentos PDF o boletines oficiales.
* **Para Agentes de IA / RAG:** Disponer de contexto limpio, libre de ruido visual, con metadatos estructurados para un enrutamiento preciso y eficiente de respuestas.

---

## 📁 Estructura del Repositorio (Taxonomía Canónica Simétrica)

Tanto el ámbito estatal como el autonómico siguen estrictamente la taxonomía de **9 categorías canónicas**:

```text
open-lex-edu/
├── README.md                           # Guía del repositorio e instrucciones para IAs
├── index.yaml                          # Índice global y grafo de relaciones autogenerado
├── schema/
│   └── norm_schema.json                # JSON Schema de validación OKF
├── estatal/                            # Normativa del Estado (BOE)
│   ├── 01_marco_normativo_general_y_organico/
│   ├── 02_gestion_y_administracion_centros/
│   ├── 03_ordenacion_curricular_y_ensenanzas/
│   ├── 04_organizacion_escolar_y_funcionamiento/
│   ├── 05_alumnado_y_servicios_escolares/
│   ├── 06_atencion_diversidad_y_orientacion/
│   ├── 07_convivencia_bienestar_y_protocolos/
│   ├── 08_personal_docente/
│   └── 09_personal_laboral_y_no_docente/
└── autonómica/
    └── canarias/                       # Normativa de Canarias (BOC / Juriscan)
        ├── 01_marco_normativo_general_y_organico/
        ├── 02_gestion_y_administracion_centros/
        ├── 03_ordenacion_curricular_y_ensenanzas/
        ├── 04_organizacion_escolar_y_funcionamiento/
        ├── 05_alumnado_y_servicios_escolares/
        ├── 06_atencion_diversidad_y_orientacion/
        ├── 07_convivencia_bienestar_y_protocolos/
        ├── 08_personal_docente/
        └── 09_personal_laboral_y_no_docente/
```

---

## ⚙️ Especificación del Frontmatter OKF (YAML)

Cada archivo `.md` contiene un bloque de encabezado YAML estructurado:

```yaml
---
id: norm-can-o-2022-05-13-eval-bachillerato
codigo_sintetizado: "O13_05_2022 Evaluacion en Bachillerato"
titulo: "Orden de 13 de mayo de 2022, por la que se regula la evaluación en Bachillerato..."
jurisdiccion: "Canarias"
ambito: "Autonómico"
organo_emisor: "Consejería de Educación, Universidades, Cultura y Deportes"
tipo_disposicion: "Orden"
numero_disposicion: "s/n"
fecha_disposicion: "2022-05-13"
fecha_publicacion: "2022-05-23"
boletin: "BOC"
numero_boletin: "100"
estado: "Vigente"
redaccion: "libro_azul" # Opciones: 'original', 'consolidada' (BOE), 'libro_azul' (Juriscan)
fuente_oficial: "https://www.gobiernodecanarias.org/boc/2022/100/001.html"
fuente_juriscan: "https://www.gobiernodecanarias.org/juriscan/ficha.jsp?id=XXXXX"

clasificacion:
  categoria_canonica: "03_ordenacion_curricular_y_ensenanzas"
  subcategoria: "Bachillerato"

tags:
  - bachillerato
  - evaluacion
  - canarias

relaciones:
  desarrolla:
    - norma_id: "norm-es-rd-243-2022"
      articulos_origen: ["Todos"]
      articulos_destino: ["13", "14", "15"]

fundamentos_derecho:
  - norma_id: "norm-es-lo-2-2006"
    articulos: ["36", "37"]
---
```

---

## 🤝 Cómo Contribuir

1. Clona el repositorio.
2. Añade o actualiza la norma en Markdown con su encabezado YAML en la carpeta canónica correspondiente.
3. Actualiza el archivo `index.yaml`.
4. Envía tu Pull Request.

---

## 📄 Licencia y Atribución

El trabajo de recopilación, estructuración, metadatos y formato OKF contenido en este repositorio se distribuye bajo la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Requisitos de Atribución

Si utilizas, adaptas o creas obras derivadas a partir de este repositorio (incluyendo su integración en bases de datos para sistemas RAG, agentes de IA o aplicaciones), **debes incluir la siguiente mención explícita**:

> *Basado en el repositorio [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu) creado por **Norberto Martín Afonso**, distribuido bajo licencia CC BY-SA 4.0.*
