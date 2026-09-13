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
| **Estatal** | BOE (Legislación Consolidada y Sección I) | **2026-09-11** | 146 normas | Incorporación del Real Decreto 722/2026 de modificación del Reglamento del Consejo General de Formación Profesional; LOE-LOMLOE, FP, EOI (RD 1041/2017) y Reales Decretos 2025-2026 (100.0% íntegra, 0 incidencias) |
| **Canarias** | BOC (Boletín Oficial de Canarias) / Portal de Educación | **2026-09-11** | 223 normas | Incorporación del Decreto 132/2026 de transformación del IES San Marcos en CIFP y de la Resolución 689/2026 de instrucciones de comedores en aulas enclave y CEE para el curso 2026-2027; instrucciones de inicio de curso 2026-2027 y protocolos vigentes (100.0% íntegra, 0 incidencias) |
| **Madrid** | BOCM / Portal de Educación de la Comunidad de Madrid | **2026-09-11** | 139 normas | Incorporación de la Orden 3206/2026 de modificación de planes de estudios de Enseñanzas Artísticas Superiores, Orden 3630/2026 de becas de comedor escolar 2026-2027 y restitución íntegra del Decreto 59/2024 de ordenación curricular y centros bilingües; instrucciones de inicio de curso 2026-2027 y protocolos vigentes (100.0% íntegra, 0 incidencias) |
| **Andalucía** | BOJA (Boletín Oficial de la Junta de Andalucía) / Portal de la Consejería | **2026-09-11** | 136 normas | Incorporación del Decreto 483/2026 de medidas de funcionamiento y actividad docente, Orden de 31 de agosto de 2026 de organización y teletrabajo docente, y Decreto 194/2026 de estructura orgánica de la Consejería de Educación; saneamiento de metadatos de clasificación; instrucciones de inicio de curso 2026-2027 y protocolos vigentes (100.0% íntegra, 0 incidencias) |

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
