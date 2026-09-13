# 📚 open-lex-edu (Open Knowledge Format - Normativa Educativa)

Base de conocimiento estructurada basada en la especificación **Open Knowledge Format (OKF)** para la gestión, consulta y procesamiento por Inteligencia Artificial y agentes de la legislación educativa en España (**Estatal** y **Autonómica: 17 Comunidades Autónomas y 2 Ciudades Autónomas**).

---

<!-- AI_AGENT_INSTRUCTIONS_START -->
> [!IMPORTANT]
> **INSTRUCTIONS FOR AI AGENTS & LLMs**
> 
> 1. **Autonomous & Self-Sufficient Corpus:** `open-lex-edu` is a fully autonomous, self-contained normative repository. When auditing, updating, or transcribing regulations, consult directly the official gazettes and portals according to the master guide **[`ESTRATEGIAS_RECOPILACION_AUTONOMICA.md`](ESTRATEGIAS_RECOPILACION_AUTONOMICA.md)**:
>    * **Estatal**: BOE (Agencia Estatal Boletín Oficial del Estado)
>    * **Canarias**: BOC (Boletín Oficial de Canarias) / Juriscan
>    * **Madrid**: BOCM (Boletín Oficial de la Comunidad de Madrid) / WLEG
>    * **Andalucía**: BOJA (Boletín Oficial de la Junta de Andalucía) / Portal Jurídico
>    * **Resto de CCAA y Ciudades Autónomas**: BOA, BOPA, BOIB, BOC, DOCM, BOCYL, DOGC, BOCCE, DOE, DOG, BOR, BOME, BORM, BON, BOPV, DOGV.
> 2. **Index First:** Read `index.yaml` first to identify relevant file paths, metadata, and cross-references.
> 3. **Metadata Headers:** Every document contains YAML frontmatter with legal scope (`jurisdiccion`, `ambito`), publication dates, status (`estado`), and consolidation type (`redaccion`).
> 4. **Recursive Legal Citations:** When processing any regulation, audit its Preamble / *Fundamentos de Derecho* to cross-reference and add any cited foundational laws or decrees directly from official sources if not yet present in `open-lex-edu`.
> 5. **Update Timestamping:** Update the *Registro de Últimas Actualizaciones* table below whenever new regulations are added.
> 6. **Departmental Instructions & Web Portals:** Do NOT limit updates strictly to official gazettes. Always audit official educational ministry web portals (`gobiernodecanarias.org/educacion/web/`, `comunidad.madrid/servicios/educacion/`, `juntadeandalucia.es/educacion/`, `educa.aragon.es`, `educastur.es`, `weib.caib.es`, `educantabria.es`, `educa.jccm.es`, `educa.jcyl.es`, `educacio.gencat.cat`, `educarex.es`, `edu.xunta.gal`, `educarioja.org`, `educarm.es`, `educacion.navarra.es`, `euskadi.eus/educacion`, `ceice.gva.es`, etc.) for start-of-course instructions, circulars, and resolutions (child wellbeing/protection coordinators, educational psychologists, teacher induction/practice phases, and vocational training innovation networks).
<!-- AI_AGENT_INSTRUCTIONS_END -->

---


## 📅 Registro de Últimas Actualizaciones Normativas

| Ámbito / Comunidad Autónoma | Fuente Oficial de Referencia | Fecha de Última Actualización | Normas Totales OKF | Cobertura de Curso Escolar |
| :--- | :--- | :---: | :---: | :---: |
| **Estatal** | BOE (Legislación Consolidada y Sección I) | **2026-09-13** | 146 normas | Marco orgánico estatal completo (LOE-LOMLOE, EBEP, Reales Decretos curriculares RD 95/2022, RD 157/2022, RD 217/2022, RD 243/2022, FP y Reales Decretos 2025-2026; 100.0% íntegra, 0 incidencias) |
| **Canarias** | BOC (Boletín Oficial de Canarias) / Portal de Educación | **2026-09-13** | 223 normas | Marco canónico canario completo, Decretos curriculares D 30/2023, D 34/2023, D 36/2023, D 37/2023, ROC D 81/2010, instrucciones de inicio de curso 2026-2027 y protocolos (100.0% íntegra, 0 incidencias) |
| **Madrid** | BOCM / Portal de Educación de la Comunidad de Madrid | **2026-09-13** | 139 normas | Marco autonómico madrileño, Decretos curriculares D 36/2022, D 61/2022, D 64/2022, D 65/2022, D 59/2024 bilingüe, órdenes de evaluación, instrucciones 2026-2027 y protocolos (100.0% íntegra, 0 incidencias) |
| **Andalucía** | BOJA (Boletín Oficial de la Junta de Andalucía) / Portal de la Consejería | **2026-09-13** | 136 normas | Marco autonómico andaluz, Decretos curriculares D 100/2023, D 101/2023, D 102/2023, D 103/2023, ROCs, instrucciones 2026-2027 y protocolos (100.0% íntegra, 0 incidencias) |
| **Resto de CCAA (14 CCAA)** | Diarios Oficiales Autonómicos (BOA, BOPA, BOIB, BOC, DOCM, BOCYL, DOGC, DOE, DOG, BOR, BORM, BON, BOPV, DOGV) | **2026-09-13** | 52 normas | Incorporación completa de los Decretos y Órdenes de ordenación y currículos LOMLOE de todas las etapas (Infantil, Primaria, ESO y Bachillerato) para Aragón, Asturias, Baleares, Cantabria, Castilla-La Mancha, Castilla y León, Cataluña, Extremadura, Galicia, La Rioja, Murcia, Navarra, País Vasco y Comunitat Valenciana (100.0% íntegra, 0 incidencias) |
| **TOTAL OPEN-LEX-EDU** | **Consolidación Diarios Oficiales del Estado y CCAA** | **2026-09-13** | **696 normas** | **Cobertura 100% íntegra nacional de enseñanzas mínimas y currículos autonómicos LOMLOE para todas las comunidades autónomas** |

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
    ├── andalucía/                      # Normativa de Andalucía (BOJA)
    ├── aragón/                         # Estructura canónica autonómica (BOA)
    ├── asturias/                       # Estructura canónica autonómica (BOPA)
    ├── baleares/                       # Estructura canónica autonómica (BOIB)
    ├── canarias/                       # Normativa de Canarias (BOC / Juriscan)
    ├── cantabria/                      # Estructura canónica autonómica (BOC)
    ├── castilla_la_mancha/             # Estructura canónica autonómica (DOCM)
    ├── castilla_y_león/                # Estructura canónica autonómica (BOCYL)
    ├── cataluña/                       # Estructura canónica autonómica (DOGC)
    ├── ceuta/                          # Estructura canónica autonómica (BOCCE)
    ├── extremadura/                    # Estructura canónica autonómica (DOE)
    ├── galicia/                        # Estructura canónica autonómica (DOG)
    ├── la_rioja/                       # Estructura canónica autonómica (BOR)
    ├── madrid/                         # Normativa de Madrid (BOCM / WLEG)
    ├── melilla/                        # Estructura canónica autonómica (BOME)
    ├── murcia/                         # Estructura canónica autonómica (BORM)
    ├── navarra/                        # Estructura canónica autonómica (BON)
    ├── país_vasco/                     # Estructura canónica autonómica (BOPV)
    └── valencia/                       # Estructura canónica autonómica (DOGV)
```

---

## 🎓 Cobertura Nacional de Currículos Autonómicos LOMLOE

El repositorio cuenta con **cobertura curricular completa (100%)** para todas las etapas educativas oficiales bajo la **LOMLOE** (Ley Orgánica 3/2020) en el marco de las 17 Comunidades Autónomas, organizadas en la categoría canónica `03_ordenacion_curricular_y_ensenanzas`:

* **Marco Estatal de Enseñanzas Mínimas (BOE)**:
  * Infantil: [Real Decreto 95/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/estatal/03_ordenacion_curricular_y_ensenanzas/RD95_2022_ensenanzas_minimas_educacion_infantil.md)
  * Primaria: [Real Decreto 157/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/estatal/03_ordenacion_curricular_y_ensenanzas/RD157_2022_ensenanzas_minimas_educacion_primaria.md)
  * ESO: [Real Decreto 217/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/estatal/03_ordenacion_curricular_y_ensenanzas/RD217_2022_ensenanzas_minimas_educacion_secundaria_obligatoria.md)
  * Bachillerato: [Real Decreto 243/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/estatal/03_ordenacion_curricular_y_ensenanzas/RD243_2022_ensenanzas_minimas_bachillerato.md)
* **Desarrollo Autonómico de Currículos (Diarios Oficiales CCAA)**:
  * **Andalucía (BOJA)**: D 100/2023 (Infantil), D 101/2023 (Primaria), D 102/2023 (ESO), D 103/2023 (Bachillerato).
  * **Aragón (BOA)**: Orden ECD/853/2022 (Infantil), Orden ECD/1112/2022 (Primaria), Orden ECD/1172/2022 (ESO), Orden ECD/1173/2022 (Bachillerato).
  * **Asturias (BOPA)**: D 56/2022 (Infantil), D 57/2022 (Primaria), D 59/2022 (ESO), D 60/2022 (Bachillerato).
  * **Illes Balears (BOIB)**: D 30/2022 (Infantil), D 31/2022 (Primaria), D 32/2022 (ESO), D 33/2022 (Bachillerato).
  * **Canarias (BOC)**: D 30/2023 (Infantil y Primaria), D 34/2023 (ESO), D 36/2023 y D 37/2023 (Bachillerato).
  * **Cantabria (BOC)**: D 66/2022 (Infantil y Primaria), D 73/2022 (ESO y Bachillerato).
  * **Castilla-La Mancha (DOCM)**: D 80/2022 (Infantil), D 81/2022 (Primaria), D 82/2022 (ESO), D 83/2022 (Bachillerato).
  * **Castilla y León (BOCYL)**: D 37/2022 (Infantil), D 38/2022 (Primaria), D 39/2022 (ESO), D 40/2022 (Bachillerato).
  * **Cataluña (DOGC)**: D 21/2023 (Infantil), D 175/2022 (Básica: Primaria y ESO), D 171/2022 (Bachillerato).
  * **Extremadura (DOE)**: D 98/2022 (Infantil), D 107/2022 (Primaria), D 110/2022 (ESO), D 109/2022 (Bachillerato).
  * **Galicia (DOG)**: D 150/2022 (Infantil), D 155/2022 (Primaria), D 156/2022 (ESO), D 157/2022 (Bachillerato).
  * **La Rioja (BOR)**: D 36/2022 (Infantil), D 41/2022 (Primaria), D 42/2022 (ESO), D 43/2022 (Bachillerato).
  * **Madrid (BOCM)**: D 36/2022 (Infantil), D 61/2022 (Primaria), D 65/2022 (ESO), D 64/2022 (Bachillerato), D 59/2024 (Bilingüe).
  * **Región de Murcia (BORM)**: D 196/2022 (Infantil), D 209/2022 (Primaria), D 235/2022 (ESO), D 251/2022 (Bachillerato).
  * **Comunidad Foral de Navarra (BON / LexNavarra)**: DF 61/2022 (Infantil), DF 67/2022 (Primaria), DF 71/2022 (ESO), DF 72/2022 (Bachillerato).
  * **País Vasco (BOPV)**: D 75/2023 (Infantil), D 77/2023 (Básica: Primaria y ESO), D 76/2023 (Bachillerato).
  * **Comunitat Valenciana (DOGV)**: D 100/2022 (Infantil), D 106/2022 (Primaria), D 107/2022 (ESO), D 108/2022 (Bachillerato).
  * **Ceuta y Melilla (BOE)**: Ámbito de gestión directa del Ministerio de Educación regulado mediante las Órdenes Ministeriales EFP/608/2022 (Infantil), EFP/678/2022 (Primaria), EFP/754/2022 (ESO) y EFP/755/2022 (Bachillerato).

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
