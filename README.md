```markdown
# 📚 open-lex-edu

Base de conocimiento estructurada basada en la especificación **Open Knowledge Format (OKF)** para la gestión, consulta y procesamiento de la legislación educativa en España (Estatal y Autonómica).

---

<!-- AI_AGENT_INSTRUCTIONS_START -->
> [!NOTE]
> **INSTRUCTIONS FOR AI AGENTS & LLMs**
> 
> This repository is formatted using the Open Knowledge Format (OKF).
> 1. **Index First:** Do NOT scan all files if searching for a specific topic. Read `index.yaml` first to identify the relevant file paths and metadata.
> 2. **Metadata Headers:** Every document contains a YAML frontmatter with legal scope (`jurisdiccion`, `ambito`, `etapa_educativa`), publication dates, and status (`estado`).
> 3. **Canonical Sources:** Always prioritize documents marked with `estado: "Vigente"`.
<!-- AI_AGENT_INSTRUCTIONS_END -->

---

## 🎯 Objetivo

El propósito de este repositorio es ofrecer la normativa jurídica de educación de forma **estructurada, versionada y en texto plano (Markdown)**. Esto permite:
* **Para personas:** Consultar leyes, reales decretos y órdenes sin la sobrecarga sintáctica de documentos PDF o boletines oficiales.
* **Para Agentes de IA / RAG:** Disponer de contexto limpio, libre de ruido visual, con metadatos estructurados para un enrutamiento preciso y eficiente de respuestas.

---

## 📁 Estructura del Repositorio

```text
.
├── README.md               # Guía del repositorio e instrucciones para IAs
├── LICENSE                 # Términos de la licencia CC BY-SA 4.0
├── index.yaml              # Índice global y mapa de enrutamiento del conocimiento
├── estatal/                # Normativa aplicable a todo el territorio nacional
│   ├── lomloe.md
│   └── rd-243-2022-bachillerato.md
└── autonómica/             # Normativa de ámbito autonómico
    └── canarias/
        └── orden-evaluacion-bachillerato.md

```

---

## ⚙️ Especificación de los Documentos (Frontmatter OKF)

Cada archivo `.md` contiene un bloque de encabezado YAML estructurado de la siguiente forma:

```yaml
---
id: norm-es-rd-243-2022
titulo: "Real Decreto 243/2022: Ordenación y enseñanzas mínimas del Bachillerato"
jurisdiccion: "España"
ambito: "Estatal" # [Estatal | Autonomico]
comunidad_autonoma: "N/A" # [Especificar si el ámbito es Autonómico, e.g., Canarias]
etapa_educativa: "Bachillerato" # [Infantil | Primaria | ESO | Bachillerato | FP]
tipo_disposicion: "Real Decreto"
fecha_publicacion: "2022-04-06"
estado: "Vigente" # [Vigente | Derogada | Modificada]
fuente_oficial: "[https://www.boe.es/eli/es/rd/2022/04/05/243](https://www.boe.es/eli/es/rd/2022/04/05/243)"
tags:
  - bachillerato
  - curriculum
  - evaluacion
---

```

---

## 🤝 Cómo Contribuir

Las aportaciones para mantener la legislación actualizada son bienvenidas:

1. Haz un **Fork** del repositorio.
2. Añade o actualiza la normativa en la carpeta correspondiente (`/estatal` o `/autonómica/<comunidad>`).
3. Asegúrate de actualizar la entrada correspondiente en el archivo `index.yaml`.
4. Abre un **Pull Request** detallando la disposición legal añadida o modificada.

---

## 📄 Licencia y Atribución

El trabajo de recopilación, estructuración, metadatos y formato OKF contenido en este repositorio se distribuye bajo la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Requisitos de Atribución

Si utilizas, adaptas o creas obras derivadas a partir de este repositorio (incluyendo su integración en bases de datos para sistemas RAG, agentes de IA o aplicaciones), **debes incluir la siguiente mención explícita**:

> *Basado en el repositorio [nmarafo/open-lex-edu](https://www.google.com/search?q=https://github.com/nmarafo/open-lex-edu) creado por **Norberto Martín Afonso**, distribuido bajo licencia CC BY-SA 4.0.*

```

```
