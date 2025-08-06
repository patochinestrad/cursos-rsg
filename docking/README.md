# Curso de Diseño de Fármacos Asistido por Computadora (CADD) y Docking

## Introducción al Diseño de Fármacos por CADD

- ¿Qué es el Diseño Racional de Fármacos?
- Tipos de enfoques:
  - Structure-Based Drug Design (SBDD)
  - Ligand-Based Drug Design (LBDD)
- Flujo general de un proyecto de CADD:
  - Selección del blanco terapéutico
  - Obtención de estructuras 3D
  - Preparación del blanco y ligandos
  - Definición del sitio blanco (gridbox)
  - Docking molecular
  - Análisis de resultados

---

## Comenzando un Proyecto de CADD

- ¿Qué se necesita para iniciar?
  - Blanco molecular definido
  - Librería de compuestos (ligandos)
  - Ensayo experimental sencillo para validar
- Importancia de un blanco validado:
  - Evidencia en literatura científica
  - Datos funcionales y terapéuticos

---

## Selección y Evaluación del Blanco Molecular

- Recursos:
  - **UniProt**: análisis funcional, dominios, localización - ¿Qué hago si no hay estructura?
  - **Literatura científica**: PubMed, ChEMBL, DrugBank
- Estructuras 3D:
  - **PDB**: elegir una con buena resolución (<2.5 Å), con los residuos , calidad general

---

## 🔹 Módulo 4: Preparación del Blanco Molecular

- Herramienta: **AutoDockTools**
  - Eliminación de aguas
  - Selección de cadenas relevantes
  - Adición de hidrógenos polares
  - Asignación de cargas (Gasteiger)
  - Exportación a PDBQT
- Visualización: **PyMOL**

---

## 🔹 Módulo 5: Preparación de los Ligandos

- Recursos:
  - **PubChem**, **ZINC**, **ChEMBL**
- Procesamiento:
  - Conversión a formato PDB (Open Babel o similares)
- Preparación con **AutoDockTools**:
  - Hidrógenos, cargas de Gasteiger
  - Definición de torsiones rotables
  - Conversión a PDBQT

---

## 🔹 Módulo 6: Definición del Sitio Activo (Gridbox)

- Métodos para seleccionar el centro:
  - Usar ligando co-cristalizado
  - Selección visual de cavidades
- Herramienta: **AutoDockTools**
  - Coordenadas XYZ
  - Dimensiones del grid

---

## 🔹 Módulo 7: Docking Molecular

- Herramienta: **AutoDock Vina**
  - Parámetros principales:
    - `--exhaustiveness`
    - `--num_modes`
  - Ejecución por línea de comandos
  - Archivos de salida: `.log`, `.pdbqt` (poses)

---

## 🔹 Módulo 8: Análisis de Resultados

- Visualización de poses:
  - **AutoDockTools**
  - **PyMOL**
- Perfil de interacciones:
  - **PLIP (Protein-Ligand Interaction Profiler)**:
    - Enlaces de hidrógeno
    - Interacciones hidrofóbicas
    - Salinas, pi-pi, cation-pi
    - Exportación de imágenes y datos
- Selección de mejores candidatos:
  - Energía de afinidad
  - Tipos y número de interacciones
  - Conformación del ligando

---

## 🔹 Módulo 9: Buenas Prácticas y Consejos Finales

- Comparación con ligando co-cristalizado
- Comprensión biológica del blanco
- Limitaciones del docking
- Reproducibilidad:
  - Registro de parámetros
  - Almacenamiento de archivos

---

## 🔹 Módulo 10 (Opcional): Próximos Pasos

- Dinámica molecular (GROMACS, MDWeb)
- Screening virtual a gran escala
- Machine Learning aplicado a priorización de compuestos

---

## 🧰 Herramientas por Etapa

| Etapa                   | Herramientas                             |
| ----------------------- | ---------------------------------------- |
| Selección del blanco    | UniProt, PubMed, PDB                     |
| Preparación del blanco  | AutoDockTools, PyMOL, Fpocket            |
| Preparación de ligandos | PubChem, ZINC, Open Babel, AutoDockTools |
| Gridbox                 | AutoDockTools, PyMOL + plugin            |
| Docking molecular       | AutoDock Vina                            |
| Análisis de resultados  | AutoDockTools, PyMOL, PLIP, Fingerprints |

---

## 📦 Recursos Extra (Opcionales)

- [AutoDock Vina GitHub](https://github.com/ccsb-scripps/AutoDock-Vina)
- [PLIP Web Server](https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index)
- [RCSB PDB](https://www.rcsb.org)
- [UniProt](https://www.uniprot.org)
