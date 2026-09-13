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
| **Resto de CCAA (14 CCAA)** | Diarios Oficiales Autonómicos (BOA, BOPA, BOIB, BOC, DOCM, BOCYL, DOGC, DOE, DOG, BOR, BORM, BON, BOPV, DOGV) | **2026-09-13** | 122 normas | Decretos y Órdenes curriculares LOMLOE completos de todas las etapas para las 14 CCAA, junto con el Lote 1 (Aragón, Cantabria, Asturias, Baleares), Lote 2 (Castilla-La Mancha, Castilla y León, Extremadura, Galicia), Lote 3 (Comunitat Valenciana, Región de Murcia, Comunidad Foral de Navarra, La Rioja) y Lote 4 (Cataluña, País Vasco, Asturias y Baleares) de Decretos y Leyes autonómicos sustantivos (100.0% íntegra, 0 incidencias) |
| **TOTAL OPEN-LEX-EDU** | **Consolidación Diarios Oficiales del Estado y CCAA** | **2026-09-13** | **766 normas** | **Cobertura 100% íntegra nacional de enseñanzas mínimas, currículos autonómicos LOMLOE y decretos/leyes autonómicos sustantivos (Lotes 1, 2, 3 y 4)** |

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

---

## 🏛️ Decretos Autonómicos Educativos Sustantivos (Lote 1)

Más allá de los currículos oficiales, se integran las disposiciones estructurales y reglamentarias que articulan el sistema educativo en cada Comunidad Autónoma:

* **Aragón (BOA)**:
  * `01_marco_normativo_general_y_organico`: [Decreto 45/2024](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/aragón/01_marco_normativo_general_y_organico/D45_2024_estructura_organica_departamento_educacion_ciencia_universidades.md) (Estructura orgánica del Departamento de Educación).
  * `05_alumnado_y_servicios_escolares`: [Decreto 51/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/aragón/05_alumnado_y_servicios_escolares/D51_2021_escolarizacion_alumnado_centros_docentes.md) (Régimen de escolarización y admisión de alumnado).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 188/2017](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/aragón/06_atencion_diversidad_y_orientacion/D188_2017_respuesta_educativa_inclusiva_convivencia.md) (Respuesta educativa inclusiva y convivencia escolar).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 73/2011](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/aragón/07_convivencia_bienestar_y_protocolos/D73_2011_carta_derechos_deberes_normas_convivencia.md) (Carta de derechos y deberes y normas de convivencia).
  * `08_personal_docente`: [Decreto 105/2013](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/aragón/08_personal_docente/D105_2013_sistema_aragones_formacion_permanente_profesorado.md) (Sistema Aragonés de Formación Permanente del Profesorado).

* **Cantabria (BOC)**:
  * `02_gestion_y_administracion_centros`: [Decreto 24/2010](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cantabria/02_gestion_y_administracion_centros/D24_2010_reglamento_organico_centros_secundaria_bachillerato_fp.md) (ROC de centros de Educación Secundaria, Bachillerato y FP).
  * `02_gestion_y_administracion_centros`: [Decreto 25/2010](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cantabria/02_gestion_y_administracion_centros/D25_2010_reglamento_organico_centros_infantil_primaria.md) (ROC de centros de Educación Infantil y Primaria).
  * `05_alumnado_y_servicios_escolares`: [Decreto 30/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cantabria/05_alumnado_y_servicios_escolares/D30_2022_modificacion_admision_alumnos_centros_docentes.md) (Admisión de alumnos en centros docentes).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 98/2005](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cantabria/06_atencion_diversidad_y_orientacion/D98_2005_ordenacion_atencion_diversidad_educacion_especial.md) (Ordenación de la atención a la diversidad y educación especial).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 53/2009](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cantabria/07_convivencia_bienestar_y_protocolos/D53_2009_convivencia_escolar_derechos_deberes.md) (Marco de convivencia escolar y derechos y deberes).

* **Principado de Asturias (BOPA)**:
  * `01_marco_normativo_general_y_organico`: [Decreto 50/2025](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/asturias/01_marco_normativo_general_y_organico/D50_2025_estructura_organica_basica_consejeria_educacion.md) (Estructura orgánica básica de la Consejería de Educación).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 147/2014](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/asturias/06_atencion_diversidad_y_orientacion/D147_2014_orientacion_educativa_profesional.md) (Orientación educativa y profesional).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 7/2019](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/asturias/07_convivencia_bienestar_y_protocolos/D7_2019_modificacion_derechos_deberes_alumnado_normas_convivencia.md) (Derechos y deberes del alumnado y normas de convivencia).
  * `08_personal_docente`: [Ley 3/2013](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/asturias/08_personal_docente/L3_2013_medidas_autoridad_profesorado.md) (Medidas de autoridad del profesorado).

* **Illes Balears (BOIB)**:
  * `02_gestion_y_administracion_centros`: [Decreto 4/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/baleares/02_gestion_y_administracion_centros/D4_2023_reglamento_organico_escuelas_infantiles_publicas_primer_ciclo.md) (ROC de las escuelas infantiles públicas de primer ciclo).
  * `05_alumnado_y_servicios_escolares`: [Decreto 64/2019](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/baleares/05_alumnado_y_servicios_escolares/D64_2019_regimen_admision_alumnos_centros_docentes.md) (Régimen de admisión de alumnos en centros sostenidos con fondos públicos).
  * `05_alumnado_y_servicios_escolares`: [Decreto 30/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/baleares/05_alumnado_y_servicios_escolares/D30_2023_transporte_escolar_centros_educativos_publicos.md) (Regulación del servicio de transporte escolar en centros públicos).

## 🏛️ Decretos y Leyes Autonómicos Educativos Sustantivos (Lote 2)

Incorporación y transcripción íntegra de la normativa educativa sustantiva y reglamentos estructurales del segundo bloque de Comunidades Autónomas:

* **Castilla-La Mancha (DOCM)**:
  * `01_marco_normativo_general_y_organico`: [Ley 7/2010](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_la_mancha/01_marco_normativo_general_y_organico/L7_2010_educacion_castilla_la_mancha.md) (Ley de Educación de Castilla-La Mancha).
  * `02_gestion_y_administracion_centros`: [Ley 3/2007](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_la_mancha/02_gestion_y_administracion_centros/L3_2007_participacion_social_educacion.md) (Participación Social en la Educación y Consejos Escolares).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 85/2018](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_la_mancha/06_atencion_diversidad_y_orientacion/D85_2018_inclusion_educativa_alumnado.md) (Inclusión educativa del alumnado de Castilla-La Mancha).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 92/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_la_mancha/06_atencion_diversidad_y_orientacion/D92_2022_organizacion_orientacion_academica_educativa_profesional.md) (Organización de la orientación académica, educativa y profesional).
  * `08_personal_docente`: [Ley 3/2012](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_la_mancha/08_personal_docente/L3_2012_autoridad_profesorado.md) (Autoridad del Profesorado de Castilla-La Mancha).

* **Castilla y León (BOCYL)**:
  * `01_marco_normativo_general_y_organico`: [Decreto 14/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_y_león/01_marco_normativo_general_y_organico/D14_2022_estructura_organica_consejeria_educacion.md) (Estructura orgánica de la Consejería de Educación).
  * `02_gestion_y_administracion_centros`: [Ley 3/1999](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_y_león/02_gestion_y_administracion_centros/L3_1999_consejo_escolar_castilla_leon.md) (Consejo Escolar de Castilla y León).
  * `03_ordenacion_curricular_y_ensenanzas`: [Ley 3/2002](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_y_león/03_ordenacion_curricular_y_ensenanzas/L3_2002_educacion_personas_adultas.md) (Educación de Personas Adultas de Castilla y León).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 51/2007](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_y_león/07_convivencia_bienestar_y_protocolos/D51_2007_derechos_deberes_alumnos_normas_convivencia_disciplina.md) (Derechos y deberes de los alumnos y normas de convivencia y disciplina escolar).
  * `08_personal_docente`: [Ley 3/2014](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/castilla_y_león/08_personal_docente/L3_2014_autoridad_profesorado.md) (Autoridad del Profesorado de Castilla y León).

* **Extremadura (DOE)**:
  * `01_marco_normativo_general_y_organico`: [Ley 4/2011](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/extremadura/01_marco_normativo_general_y_organico/L4_2011_educacion_extremadura.md) (Ley de Educación de Extremadura).
  * `01_marco_normativo_general_y_organico`: [Decreto 237/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/extremadura/01_marco_normativo_general_y_organico/D237_2023_estructura_organica_consejeria_educacion_ciencia_fp.md) (Estructura orgánica de la Consejería de Educación, Ciencia y Formación Profesional).
  * `05_alumnado_y_servicios_escolares`: [Decreto 128/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/extremadura/05_alumnado_y_servicios_escolares/D128_2021_admision_alumnado_centros_docentes_sostenidos_fondos_publicos.md) (Admisión del alumnado en centros docentes sostenidos con fondos públicos).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 228/2014](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/extremadura/06_atencion_diversidad_y_orientacion/D228_2014_respuesta_educativa_diversidad_alumnado.md) (Respuesta educativa a la diversidad del alumnado).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 50/2007](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/extremadura/07_convivencia_bienestar_y_protocolos/D50_2007_derechos_deberes_alumnado_normas_convivencia.md) (Derechos y deberes del alumnado y normas de convivencia en centros docentes).

* **Galicia (DOG)**:
  * `01_marco_normativo_general_y_organico`: [Decreto 138/2024](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/galicia/01_marco_normativo_general_y_organico/D138_2024_estrutura_organica_conselleria_educacion_ciencia_universidades_fp.md) (Estructura orgánica de la Consellería de Educación, Ciencia, Universidades y FP).
  * `05_alumnado_y_servicios_escolares`: [Decreto 13/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/galicia/05_alumnado_y_servicios_escolares/D13_2022_admision_alumnado_centros_docentes_sostenidos_fondos_publicos.md) (Admisión de alumnado en centros docentes sostenidos con fondos públicos).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 229/2011](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/galicia/06_atencion_diversidad_y_orientacion/D229_2011_atencion_diversidad_alumnado_centros_docentes.md) (Atención a la diversidad del alumnado en centros docentes).
  * `07_convivencia_bienestar_y_protocolos`: [Ley 4/2011](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/galicia/07_convivencia_bienestar_y_protocolos/L4_2011_convivencia_participacion_comunidad_educativa.md) (Convivencia y participación de la comunidad educativa).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 8/2015](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/galicia/07_convivencia_bienestar_y_protocolos/D8_2015_desarrollo_ley_convivencia_participacion_comunidad_educativa.md) (Desarrollo de la Ley de convivencia y participación de la comunidad educativa).

## 🏛️ Decretos y Leyes Autonómicos Educativos Sustantivos (Lote 3)

Incorporación y transcripción íntegra de la normativa educativa sustantiva y reglamentos estructurales del tercer bloque de Comunidades Autónomas:

* **Comunitat Valenciana (DOGV)**:
  * `01_marco_normativo_general_y_organico`: [Ley 1/2024](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/valencia/01_marco_normativo_general_y_organico/L1_2024_libertad_educativa.md) (Ley por la que se regula la libertad educativa).
  * `02_gestion_y_administracion_centros`: [Decreto 253/2019](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/valencia/02_gestion_y_administracion_centros/D253_2019_organizacion_funcionamiento_centros_infantil_primaria.md) (Organización y funcionamiento de centros de Infantil y Primaria).
  * `02_gestion_y_administracion_centros`: [Decreto 252/2019](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/valencia/02_gestion_y_administracion_centros/D252_2019_organizacion_funcionamiento_centros_secundaria_bachillerato_fp.md) (Organización y funcionamiento de centros de ESO, Bachillerato y FP).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 104/2018](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/valencia/06_atencion_diversidad_y_orientacion/D104_2018_principios_equidad_inclusion_sistema_educativo.md) (Principios de equidad y de inclusión en el sistema educativo valenciano).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 72/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/valencia/06_atencion_diversidad_y_orientacion/D72_2021_organizacion_orientacion_educativa_profesional.md) (Organización de la orientación educativa y profesional).

* **Región de Murcia (BORM)**:
  * `02_gestion_y_administracion_centros`: [Ley 6/1998](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/murcia/02_gestion_y_administracion_centros/L6_1998_consejos_escolares_region_murcia.md) (Consejos Escolares de la Región de Murcia).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 359/2009](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/murcia/06_atencion_diversidad_y_orientacion/D359_2009_respuesta_educativa_diversidad_alumnado.md) (Respuesta educativa a la diversidad del alumnado en la Región de Murcia).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 16/2016](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/murcia/07_convivencia_bienestar_y_protocolos/D16_2016_normas_convivencia_centros_docentes.md) (Normas de convivencia en los centros docentes).
  * `07_convivencia_bienestar_y_protocolos`: [Ley 7/2007](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/murcia/07_convivencia_bienestar_y_protocolos/L7_2007_igualdad_mujeres_hombres_proteccion_violencia_genero.md) (Igualdad entre Mujeres y Hombres y Protección contra la Violencia de Género).
  * `08_personal_docente`: [Ley 1/2013](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/murcia/08_personal_docente/L1_2013_autoridad_docente_region_murcia.md) (Autoridad docente de la Región de Murcia).

* **Comunidad Foral de Navarra (BON / LexNavarra)**:
  * `01_marco_normativo_general_y_organico`: [Decreto Foral 245/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/navarra/01_marco_normativo_general_y_organico/DF245_2023_estructura_organica_departamento_educacion.md) (Estructura orgánica del Departamento de Educación).
  * `02_gestion_y_administracion_centros`: [Decreto Foral 24/1997](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/navarra/02_gestion_y_administracion_centros/DF24_1997_reglamento_organico_institutos_educacion_secundaria.md) (ROC de los Institutos de Educación Secundaria).
  * `02_gestion_y_administracion_centros`: [Ley Foral 12/1997](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/navarra/02_gestion_y_administracion_centros/LF12_1997_consejo_escolar_navarra.md) (Consejo Escolar de Navarra).
  * `05_alumnado_y_servicios_escolares`: [Decreto Foral 33/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/navarra/05_alumnado_y_servicios_escolares/DF33_2021_admision_alumnado_centros_docentes.md) (Admisión del alumnado en centros docentes públicos y concertados).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto Foral 47/2010](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/navarra/07_convivencia_bienestar_y_protocolos/DF47_2010_derechos_deberes_alumnado_convivencia_centros.md) (Derechos y deberes del alumnado y convivencia escolar).

* **La Rioja (BOR)**:
  * `01_marco_normativo_general_y_organico`: [Decreto 53/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/la_rioja/01_marco_normativo_general_y_organico/D53_2023_estructura_organica_consejeria_educacion_empleo.md) (Estructura orgánica de la Consejería de Educación y Empleo).
  * `02_gestion_y_administracion_centros`: [Ley 3/2004](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/la_rioja/02_gestion_y_administracion_centros/L3_2004_consejos_escolares_la_rioja.md) (Consejos Escolares de La Rioja).
  * `05_alumnado_y_servicios_escolares`: [Decreto 24/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/la_rioja/05_alumnado_y_servicios_escolares/D24_2021_procedimiento_admision_alumnado_centros_docentes.md) (Procedimiento de admisión del alumnado en centros docentes).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 4/2009](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/la_rioja/07_convivencia_bienestar_y_protocolos/D4_2009_convivencia_escolar_derechos_deberes_comunidad_educativa.md) (Convivencia escolar y derechos y deberes de la comunidad educativa).
  * `08_personal_docente`: [Ley 2/2011](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/la_rioja/08_personal_docente/L2_2011_autoridad_profesor_convivencia_centros_docentes.md) (Autoridad del profesor y convivencia en centros docentes).

## 🏛️ Decretos y Leyes Autonómicos Educativos Sustantivos (Lote 4)

Incorporación y transcripción íntegra de la normativa educativa sustantiva y reglamentos estructurales del cuarto bloque de Comunidades Autónomas, completando la cobertura nacional simétrica (17 Comunidades Autónomas con su bloque troncal de mínimo 5 leyes/decretos estructurales):

* **Cataluña (DOGC / BOE)**:
  * `01_marco_normativo_general_y_organico`: [Ley 12/2009](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cataluña/01_marco_normativo_general_y_organico/L12_2009_educacion_cataluna.md) (Ley de Educación de Cataluña - LEC).
  * `01_marco_normativo_general_y_organico`: [Decreto 59/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cataluña/01_marco_normativo_general_y_organico/D59_2022_reestructuracion_departamento_educacion.md) (Reestructuración del Departamento de Educación).
  * `02_gestion_y_administracion_centros`: [Decreto 102/2010](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cataluña/02_gestion_y_administracion_centros/D102_2010_autonomia_centros_educativos.md) (Autonomía de los centros educativos).
  * `05_alumnado_y_servicios_escolares`: [Decreto 11/2021](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cataluña/05_alumnado_y_servicios_escolares/D11_2021_programacion_oferta_educativa_procedimiento_admision.md) (Programación de la oferta educativa y del procedimiento de admisión).
  * `06_atencion_diversidad_y_orientacion`: [Decreto 150/2017](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/cataluña/06_atencion_diversidad_y_orientacion/D150_2017_atencion_educativa_alumnado_sistema_inclusivo.md) (Atención educativa al alumnado en el marco de un sistema inclusivo).

* **País Vasco (BOPV / BOE)**:
  * `01_marco_normativo_general_y_organico`: [Ley 17/2023](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/país_vasco/01_marco_normativo_general_y_organico/L17_2023_educacion_pais_vasco.md) (Ley de Educación del País Vasco).
  * `01_marco_normativo_general_y_organico`: [Decreto 381/2024](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/país_vasco/01_marco_normativo_general_y_organico/D381_2024_estructura_organica_funcional_departamento_educacion.md) (Estructura orgánica y funcional del Departamento de Educación).
  * `02_gestion_y_administracion_centros`: [Ley 13/1988](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/país_vasco/02_gestion_y_administracion_centros/L13_1988_consejos_escolares_euskadi.md) (Consejos Escolares de Euskadi).
  * `05_alumnado_y_servicios_escolares`: [Decreto 1/2018](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/país_vasco/05_alumnado_y_servicios_escolares/D1_2018_admision_escolarizacion_alumnado_centros_docentes.md) (Admisión y escolarización del alumnado en centros docentes públicos y concertados).
  * `07_convivencia_bienestar_y_protocolos`: [Decreto 201/2008](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/país_vasco/07_convivencia_bienestar_y_protocolos/D201_2008_derechos_deberes_alumnado_convivencia_centros.md) (Derechos y deberes de los alumnos y alumnas y normas de convivencia en centros docentes no universitarios).

* **Principado de Asturias (BOPA / BOE - Complemento Troncal)**:
  * `02_gestion_y_administracion_centros`: [Ley 9/1996](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/asturias/02_gestion_y_administracion_centros/L9_1996_consejo_escolar_principado_asturias.md) (Consejo Escolar del Principado de Asturias).

* **Illes Balears (BOIB / BOE - Complemento Troncal)**:
  * `01_marco_normativo_general_y_organico`: [Ley 1/2022](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/baleares/01_marco_normativo_general_y_organico/L1_2022_educacion_illes_balears.md) (Ley de Educación de las Illes Balears - LEIB).
  * `02_gestion_y_administracion_centros`: [Ley 9/1998](file:///c:/Users/norbe/Documents/Normativa Actualizada 2026/open-lex-edu/autonómica/baleares/02_gestion_y_administracion_centros/L9_1998_consejos_escolares_illes_balears.md) (Consejos Escolares de las Illes Balears).

---

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

## 💡 Cómo usar open-lex-edu en Google NotebookLM

`open-lex-edu` está especialmente optimizado para ser consumido como fuente de conocimiento en **[Google NotebookLM](https://notebooklm.google.com/)**, permitiendo realizar consultas jurídicas, auditorías normativas, resolución de supuestos prácticos de Inspección y fundamentación legal en minutos con cero alucinaciones:

1. **Crear un Nuevo Cuaderno**: Entra en [Google NotebookLM](https://notebooklm.google.com/) y pulsa en **Nuevo Cuaderno**.
2. **Añadir la Web o Archivos como Fuente**:
   - **Vía Web**: En la ventana de fuentes, selecciona **Sitio web** e introduce la URL del repositorio: `https://github.com/nmarafo/open-lex-edu` (o los enlaces web a las normas o carpetas autonómicas que desees consultar).
   - **Vía Archivos Markdown / Drive**: También puedes subir directamente los archivos `.md` de la normativa que vayas a utilizar (por ejemplo, las enseñanzas mínimas estatales y los decretos u órdenes de tu Comunidad Autónoma).
3. **Configurar Respuesta y Prompt Maestro**:
   - Abre la configuración del cuaderno (icono de ajustes en el panel de chat o barra lateral).
   - En longitud de respuesta, selecciona **"Más Larga"**.
   - En las instrucciones personalizadas del cuaderno, pega el [Prompt Maestro Universal](#-prompt-maestro-para-agentes-de-ia-y-llms-gemini-claude-gpt-deepseek-ollama-notebooklm).
4. **Iniciar el Agente**: Guarda los ajustes y escribe en el chat la palabra:
   ```text
   Comenzar
   ```
   *(El agente te solicitará tu Comunidad Autónoma, etapa educativa, rol profesional y el objeto de la consulta).*

---

## 🤖 Prompt Maestro para Agentes de IA y LLMs (Gemini, Claude, GPT, DeepSeek, Ollama, NotebookLM)

Para optimizar la interacción, consulta jurídica y explotación del repositorio con modelos de lenguaje y agentes de IA, se proporciona el siguiente **Prompt Maestro Universal**. Diseñado para integrarse en el *System Prompt*, *Custom Instructions*, *Gems*, *Projects* o al inicio de sesiones de trabajo:

<details open>
<summary><b>📋 Haz clic para desplegar / copiar el Prompt Maestro Universal</b></summary>

```markdown
# ROL Y MISIÓN
Actúa como un Consultor Jurídico de Élite e Inspector de Educación del Estado Español, con dominio absoluto del Derecho Administrativo Educativo y del repositorio normativo estructurado «open-lex-edu». Tu cometido es asesorar, dictaminar, fundamentar y resolver cualquier consulta técnica, docente, directiva o de inspección con rigor jurídico estricto, precisión literal y cero alucinaciones.

Si el usuario escribe únicamente «Comenzar», responde presentándote brevemente con tu rol institucional y solicita al usuario los 4 parámetros del contexto de consulta para orientar el dictamen.

---

# ARQUITECTURA DE CONOCIMIENTO (open-lex-edu / OKF)
Toda tu fundamentación debe anclarse en la taxonomía y metadatos de open-lex-edu:
1. Formato Open Knowledge Format (OKF): Archivos Markdown con cabecera YAML estructurada (id, titulo, jurisdiccion, ambito, tipo_disposicion, numero_disposicion, fecha_publicacion, boletin, estado: Vigente|Derogada|Modificada, redaccion: original|consolidada|libro_azul, clasificacion, tags, relaciones).
2. Las 9 Categorías Canónicas:
   - 01_marco_normativo_general_y_organico (CE, LOE-LOMLOE, EBEP, LPAC 39/2015, Leyes autonómicas)
   - 02_gestion_y_administracion_centros (Autonomía, presupuestos, conciertos, órganos colegiados)
   - 03_ordenacion_curricular_y_ensenanzas (RDs de mínimas 95/157/217/243/2022 y Decretos/Órdenes autonómicos)
   - 04_organizacion_escolar_y_funcionamiento (ROCs, calendarios, horarios, instrucciones anuales de curso)
   - 05_alumnado_y_servicios_escolares (Admisión, transporte, comedor, gratuidad de libros, títulos)
   - 06_atencion_diversidad_y_orientacion (NEAE, inclusión, adaptación curricular, aulas enclave/específicas)
   - 07_convivencia_bienestar_y_protocolos (LOPIVI, Ley Libertad Sexual, acoso escolar, ciberacoso, suicidio)
   - 08_personal_docente (RD 276/2007, listas de interinos, licencias, permisos, evaluación docente)
   - 09_personal_laboral_y_no_docente (Convenios laborales, auxiliares educativos, fisioterapeutas)
3. Distribución Territorial:
   - Estatal: España (BOE - Legislación Consolidada).
   - Autonómico: 17 Comunidades Autónomas y 2 Ciudades Autónomas (BOC, BOCM, BOJA, BOA, DOGC, DOGV, etc.).

---

# REGLAS DE ORO DE RAZONAMIENTO JURÍDICO (ANTI-ALUCINACIÓN)

1. PRINCIPIO DE JERARQUÍA NORMATIVA (Art. 9.3 CE y Art. 1.2 Código Civil):
   - Constitución Española > Leyes Orgánicas (LOE/LOMLOE, LOPIVI) > Leyes Ordinarias autonómicas > Reales Decretos estatales > Decretos autonómicos > Órdenes ministeriales/consejería > Resoluciones e Instrucciones de inicio de curso.
   - Una norma inferior nunca puede contradecir ni restringir derechos reconocidos por una superior.

2. DISTRIBUCIÓN COMPETENCIAL (Art. 149.1.1ª, 18ª y 30ª CE):
   - Distingue con total nitidez entre la competencia básica estatal (ej. Enseñanzas Mínimas, condiciones de obtención de títulos, EBEP) y la competencia autonómica de desarrollo y ejecución (currículo autonómico, ROC, instrucciones de funcionamiento, ratios, gestión de personal).
   - Jamás apliques una norma autonómica de una Comunidad en el territorio de otra a menos que se trate de un estudio de derecho comparado expresamente solicitado.

3. VIGENCIA Y DERECHO TRANSITORIO:
   - Comprueba siempre el campo YAML `estado: Vigente`. Si citas una norma derogada o en redacción original previa a su modificación, debes advertirlo explícitamente y señalar la norma modificadora o derogatoria (campo `relaciones.modifica` o `relaciones.deroga`).
   - Diferencia la redacción original de la redacción consolidada vigente para el curso escolar actual.

4. CERO APROXIMACIONES EN ARTICULADO:
   - Cita siempre con precisión: Disposición, Número, Año, Título, Artículo, Apartado y Letra (ejemplo: «Art. 121.2 de la Ley Orgánica 2/2006 (LOE), modificada por la LOMLOE», o «Art. 14.3 del Decreto 157/2022 / Decreto autonómico correspondiente»).
   - Si no tienes certeza absoluta de un número de artículo o anexo específico en el corpus cargado, indica la disposición y advierte que debe verificarse en el texto oficial, prohibiéndose expresamente inventar artículos.

5. PREVALENCIA DE LAS INSTRUCCIONES Y CIRCULARES DE INICIO DE CURSO:
   - Para aspectos organizativos operativos (coordinador de bienestar LOPIVI, equipos de orientación, criterios de sustitución docente, calendarios y pruebas extraordinarias), recurre a las Resoluciones e Instrucciones de la Consejería del curso escolar en vigor.

6. CONDICIONAMIENTO OBLIGATORIO DE RESPUESTAS AUTONÓMICAS Y VERIFICACIÓN PROCEDIMENTAL:
   - Si el usuario especifica una Comunidad Autónoma (ej. Canarias, Madrid, Andalucía, etc.), queda TERMINANTEMENTE PROHIBIDO emitir una conclusión afirmativa o negativa en la «Sinopsis Ejecutiva» amparándose exclusivamente en principios o directrices estatales básicas generales.
   - Es preceptivo contrastar el procedimiento administrativo, el calendario y los requisitos de expedición documental en las Instrucciones/Resoluciones de la Consejería o Departamento autonómico correspondiente.
   - Si en el contexto disponible o corpus cargado no se dispone del texto articulado de la resolución autonómica de evaluación o gestión procedimental, el agente DEBE advertirlo expresamente en la Sinopsis («La doctrina estatal básica lo ampara de forma genérica, pero el procedimiento de expedición de [CC.AA.] supedita su entrega a [condición o momento temporal] según la normativa autonómica que debe verificarse en el diario oficial autonómico»).
   - En Formación Profesional y Régimen Especial, discrimina siempre el régimen según el nivel de la oferta (Grado Básico vs. Grado Medio / Superior / Cursos de Especialización) y el plan de estudios (LO 3/2022 vs. LOE a extinguir).

---

# PROTOCOLO DE RESPUESTA OBLIGATORIO

Estructura cada dictamen o respuesta técnica según el siguiente esquema formal:

### 1. 📌 SINOPSIS EJECUTIVA
- Conclusión jurídica o directiva directa en 2-3 líneas respondiendo a la pregunta sin rodeos. En consultas autonómicas, la conclusión debe incorporar explícitamente los condicionantes temporales o procedimentales fijados por la normativa de la Comunidad Autónoma (evitando respuestas afirmativas genéricas basadas únicamente en normas estatales).

### 2. ⚖️ FUNDAMENTACIÓN JURÍDICA Y MARCO NORMATIVO APLICABLE
- Marco Estatal Básico: Citas con rango normativo (CE, LOE-LOMLOE, Reales Decretos).
- Marco Autonómico de Desarrollo: Normativa de la Comunidad Autónoma consultada (Decretos curriculares, ROC, Órdenes, Protocolos vigentes). Obligatorio identificar la disposición autonómica específica si el ámbito de consulta no es exclusivamente estatal.
- Instrucciones / Resoluciones Departamentales: Circulares del curso escolar actual aplicables y resoluciones de evaluación de la Dirección General competente.

### 3. 🔍 ANÁLISIS JURÍDICO-TÉCNICO Y ARTICULADO CLAVE
- Desglose razonado con citas textuales o literales de los artículos determinantes.
- En caso de conflicto normativo, resolución fundada en jerarquía o especialidad (lex specialis derogat legi generali).

### 4. 🛠️ PROCEDIMIENTO PRÁCTICO / PAUTAS OPERATIVAS (Para el Centro / Docente / Inspección)
- Pasos de actuación recomendados: competencia del órgano (Dirección, Claustro, Consejo Escolar, CCP, Inspección), plazos administrativos y documentos de centro a actualizar (PE, PGA, RRI/NOF, Programación Didáctica).

---

# PARÁMETROS DEL CONTEXTO DE CONSULTA:
- Ámbito Territorial / CC.AA.: [España / Canarias / Madrid / Andalucía / Otra CCAA]
- Etapa / Enseñanza: [Infantil / Primaria / ESO / Bachillerato / FP / Régimen Especial]
- Perfil del Usuario: [Docente / Equipo Directivo / Opositor / Inspector de Educación / Familia]
- Tema o Conflicto: [Describe aquí la consulta concreta]
```
</details>

### ⚙️ Guía de Adaptación por Plataforma

* **NotebookLM (Google)**: Carga en el cuaderno los archivos `.md` de `open-lex-edu` deseados y añade el prompt maestro en la primera nota de instrucción o como mensaje de encuadre en el chat.
* **Claude (Projects / System Prompt - Anthropic)**: Configúralo en las *Project Instructions*. Excelente rendimiento con modo de razonamiento extendido (*Extended Thinking*) para resolver antinomias y dictámenes jurídicos complejos.
* **ChatGPT (Custom GPT / Preamble - OpenAI)**: Pégalo en el apartado *Instructions* de tu Custom GPT. Sube `index.yaml` o las carpetas autonómicas prioritarias como archivos de *Knowledge*.
* **Gemini (Gems - Google)**: Añádelo en las instrucciones del Gem. Aprovecha la ventana de contexto de 1M-2M tokens para analizar leyes orgánicas completas y decretos curriculares extensos simultáneamente.
* **DeepSeek (V3 / R1)**: Ejecútalo directamente como preámbulo. DeepSeek-R1 desglosará la jerarquía y aplicabilidad administrativa paso a paso en su bloque de pensamiento.
* **Ollama (Modelos Locales como Llama 3 o Qwen 2.5)**: Inclúyelo en el bloque `SYSTEM """..."""` del `Modelfile`, estableciendo `PARAMETER temperature 0.1` para maximizar la fidelidad documental.

---

## 📄 Licencia y Atribución

El trabajo de recopilación, estructuración, metadatos y formato OKF contenido en este repositorio se distribuye bajo la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Requisitos de Atribución

Si utilizas, adaptas o creas obras derivadas a partir de este repositorio (incluyendo su integración en bases de datos para sistemas RAG, agentes de IA o aplicaciones), **debes incluir la siguiente mención explícita**:

> *Basado en el repositorio [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu) creado por **Norberto Martín Afonso**, distribuido bajo licencia CC BY-SA 4.0.*
