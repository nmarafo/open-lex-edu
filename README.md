# 📚 open-lex-edu (Open Knowledge Format - Normativa Educativa)

Base de conocimiento estructurada basada en la especificación **Open Knowledge Format (OKF)** para la gestión, consulta y procesamiento por Inteligencia Artificial y agentes de la legislación educativa en España (**Estatal** y **Autonómica: Canarias, Madrid y Andalucía**).

---

<!-- AI_AGENT_INSTRUCTIONS_START -->
> [!IMPORTANT]
> **INSTRUCTIONS FOR AI AGENTS & LLMs**
> 
> 1. **Autonomous & Self-Sufficient Corpus:** `open-lex-edu` is a fully autonomous, self-contained normative repository. When auditing, updating, or transcribing regulations, use directly the official gazettes and portals:
>    * **Estatal**: BOE (Agencia Estatal Boletín Oficial del Estado)
>    * **Canarias**: BOC (Boletín Oficial de Canarias) / Juriscan
>    * **Madrid**: BOCM (Boletín Oficial de la Comunidad de Madrid) / WLEG
>    * **Andalucía**: BOJA (Boletín Oficial de la Junta de Andalucía)
> 2. **Index First:** Read `index.yaml` first to identify relevant file paths, metadata, and cross-references.
> 3. **Metadata Headers:** Every document contains YAML frontmatter with legal scope (`jurisdiccion`, `ambito`), publication dates, status (`estado`), and consolidation type (`redaccion`).
> 4. **Recursive Legal Citations:** When processing any regulation, audit its Preamble / *Fundamentos de Derecho* to cross-reference and add any cited foundational laws or decrees directly from official sources if not yet present in `open-lex-edu`.
> 5. **Update Timestamping:** Update the *Registro de Últimas Actualizaciones* table below whenever new regulations are added.
> 6. **Departmental Instructions & Web Portals:** Do NOT limit updates strictly to official gazettes (BOC/BOCM/BOJA). Always audit official educational ministry web portals (`gobiernodecanarias.org/educacion/web/`, `comunidad.madrid/servicios/educacion/`, `juntadeandalucia.es/educacion/`) for start-of-course instructions, circulars, and resolutions (child wellbeing/protection coordinators, educational psychologists, teacher induction/practice phases, and vocational training innovation networks).
<!-- AI_AGENT_INSTRUCTIONS_END -->

---


## 📅 Registro de Últimas Actualizaciones Normativas

| Ámbito / Comunidad Autónoma | Fuente Oficial de Referencia | Fecha de Última Actualización | Normas Totales OKF | Cobertura de Curso Escolar |
| :--- | :--- | :---: | :---: | :---: |
| **Estatal** | BOE (Legislación Consolidada) | **2026-09-05** | 145 normas | LOE-LOMLOE, FP, EOI (RD 1041/2017) y Reales Decretos 2025-2026 |
| **Canarias** | BOC (Boletín Oficial de Canarias) / Portal de Educación | **2026-09-06** | 221 normas | Completa (100.0% íntegra, 0 incidencias; rectificación de texto auténtico de D9/2022 Admisión [40K] e incorporación de 8 normas estructurales derivadas de fundamentos de derecho: D224/2017 ROC CIFP [137K], D174/2018 Absentismo Escolar [50K], O3/3/2022 Desarrollo Admisión [33K], O5/11/2012 Préstamo de Libros [31K], O20/10/2022 EBPA Adultos [38K], O21/9/2016 Acreditación MCERL [17K], O16/3/2018 Currículo Música Elemental [147K], O7/11/2007 Evaluación Básica [64K]; junto a las instrucciones de inicio de curso 2026-2027 y protocolos vigentes; Cursos 2025-2026 / 2026-2027) |
| **Madrid** | BOCM / Portal de Educación de la Comunidad de Madrid | **2026-09-06** | 137 normas | Completa (100.0% íntegra, 0 incidencias; incorporación de 7 normas estructurales derivadas de fundamentos de derecho: D28/2024 Estructura Orgánica Consejería [11K], D9/2025 Planes de Estudio FP Grado Básico [552K], D46/2015 Coordinación Atención Temprana [40K], O2743/2023 Organización y Funcionamiento EOEP [48K], O2034/2023 Bachillerato Personas Adultas [55K], O502/2013 Jornada Escolar Continuada [19K], O2367/2025 Pruebas Bachillerato Mayores 20 Años [53K]; junto a las instrucciones de inicio de curso 2026-2027 y protocolos vigentes; Cursos 2025-2026 / 2026-2027) |
| **Andalucía** | BOJA (Boletín Oficial de la Junta de Andalucía) / Portal de la Consejería | **2026-09-06** | 133 normas | Completa (100.0% íntegra, 0 incidencias; auditoría exhaustiva de fundamentos de derecho [333 citas]; remediación y restitución de texto íntegro en D6/2017 Servicios Complementarios y Plan de Apertura [30K] y D40/2011 Criterios de Admisión [107K]; incorporación de normas estructurales derivadas de fundamentos: D152/2020 Acceso a la Función Directiva y Equipos Directivos [54K], D220/2013 Marco General de Evaluación del Sistema Educativo [24K] y D54/2022 Ordenación de Enseñanzas Artísticas Superiores [67K]; junto a las instrucciones de inicio de curso 2026-2027 y protocolos vigentes; Cursos 2025-2026 / 2026-2027) |

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
    ├── canarias/                       # Normativa de la Comunidad Autónoma de Canarias (BOC / Juriscan)
    ├── madrid/                         # Normativa de la Comunidad de Madrid (BOCM / WLEG)
    └── andalucía/                      # Normativa de la Comunidad Autónoma de Andalucía (BOJA)
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
organo_emisor: "Consejería de Educación, Formación Profesional, Actividad Física y Deportes"
tipo_disposicion: "Orden"
numero_disposicion: "s/n"
fecha_disposicion: "2022-05-13"
fecha_publicacion: "2022-05-23"
boletin: "BOC"
numero_boletin: "100"
estado: "Vigente"
redaccion: "pdf_oficial_boc"
fuente_oficial: "https://www.gobiernodecanarias.org/boc/2022/100/001.html"

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
  fundamentado_en:
    - norma_id: "norm-can-l-6-2014"
---
```

---

## 📄 Licencia y Atribución

El trabajo de recopilación, estructuración, metadatos y formato OKF contenido en este repositorio se distribuye bajo la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Requisitos de Atribución

Si utilizas, adaptas o creas obras derivadas a partir de este repositorio (incluyendo su integración en bases de datos para sistemas RAG, agentes de IA o aplicaciones), **debes incluir la siguiente mención explícita**:

> *Basado en el repositorio [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu) creado por **Norberto Martín Afonso**, distribuido bajo licencia CC BY-SA 4.0.*
