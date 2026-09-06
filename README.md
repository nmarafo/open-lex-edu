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
| **Canarias** | BOC (Boletín Oficial de Canarias) / Portal de Educación | **2026-09-06** | 213 normas | Completa (100.0% íntegra, 0 incidencias; incorporación de las instrucciones de inicio de curso 2026-2027: R1012/2026 LOPIVI [36K], Psicología Educativa [32K], R5581/2026 Prácticas Maestros [23K], Redes FP [51K]; y de los 10 protocolos e instrucciones estructurales históricos vigentes: R1/2/2024 Móviles [21K], R20/5/2026 Altas Temperaturas v3 [59K], R26/9/2024 PIRS Riesgo Suicida [250K], R18/3/2021 Protocolo Trans* [64K], R19/1/2022 Cambio Nombre Trans* [15K], R13/11/2019 Violencia de Género [54K], R23/1/2019 Absentismo Escolar [26K], R13/3/2015 Convivencia 67 [67K], I13/4/2016 Admisión Violencia Género [8K] y R11/4/2018 Comisión Resolución Conflictos [14K]; Cursos 2025-2026 / 2026-2027) |
| **Madrid** | BOCM / Portal de Educación de la Comunidad de Madrid | **2026-09-06** | 130 normas | Completa (100.0% íntegra, 0 incidencias; incorporación de las instrucciones de comienzo de curso 2026-2027 en centros públicos: I15/7/2026 con LOPIVI y bienestar [198K], R27/7/2026 regulación de la fase de prácticas del Cuerpo de Maestros BOCM n.º 186 [54K], I2/7/2024 funcionamiento de escuelas infantiles públicas [10K], I2/7/2024 funcionamiento de casas de niños [12K], I27/6/2023 primer ciclo infantil en CEIP [46K], I29/7/2026 Bachillerato de personas adultas 2026-2027 [26K], I17/7/2026 organización y funcionamiento de CEPA 2026-2027 [73K], I17/7/2026 admisión a Grado Básico en CEPA 2026-2027 [21K], I18/5/2026 incorporación a Aulas de Compensación Educativa ACE [53K] y R11/12/2025 Protocolo de Coordinación de Atención Temprana [110K]; Cursos 2025-2026 / 2026-2027) |
| **Andalucía** | BOJA (Boletín Oficial de la Junta de Andalucía) | **2026-09-06** | 118 normas | Completa (100.0% íntegra, 0 incidencias; saneamiento integral y adición por Fundamentos de Derecho: O18/9/2025 evaluación FP [156K], O26/12/2024 y O2/12/2022 convocatorias de conciertos educativos [60K], D71/2009 Censo de Entidades Colaboradoras/AMPAs [23K], D151/1997 Registro de Centros [3.7K], O16/9/2019 pruebas ESO adultos [39K], D1/2003 IACP, D55/2012 Enseñanzas Deportivas, O13/7/2007 Inspección, O24/5/2011 Provisión Docente, O19/3/2012 Conservatorios, O21/2/2017 Pruebas Acceso FP, O20/2/2020 Admisión, O19/10/2020 y O9/2/2022 Enseñanzas Artísticas Superiores, O9/11/2020 Dirección Centros, O26/7/2023 Plan General Inspección, I28/6/2024 Aulas Hospitalarias, R19/1/2026 Calendario Admisión, alineación de currículos LOMLOE Infantil, Primaria, ESO y Bachillerato; Cursos 2025-2026 / 2026-2027) |

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
