# Proyect-Scene-Graph

An interactive 3D graphics application developed in **Python** that renders a hierarchical 3D articulated character using a **Scene Graph (Scenegraph)** architecture. Implements an **OpenGL** rendering pipeline via **Pyglet** with custom GLSL shaders to articulate limbs and switch camera perspective.
##
Aplicación gráfica e interactiva desarrollada en **Python** que renderiza un personaje articulado tridimensional utilizando una jerarquía de **Grafo de Escena (Scenegraph)**. Implementa un pipeline de renderizado en **OpenGL** con **Pyglet** y shaders personalizados en GLSL para articular extremidades y alternar dinámicamente entre distintas poses dramáticas y perspectivas de cámara.

##  Academic Context

* **Institution:** Universidad de Chile
* **Course:** Modelación y computación gráfica para ingenieros
* **Purpose:** Individual project
* **Base Repository:** [cc3501-computer-graphics](https://github.com/PLUMAS-research/cc3501-computer-graphics)
##
* **Institución:** Universidad de Chile
* **Curso:** Modelación y computación gráfica para ingenieros
* **Propósito:** Proyecto individual
* **Repositorio base:** [cc3501-computer-graphics](https://github.com/PLUMAS-research/cc3501-computer-graphics)  

## Key Features

* **Hierarchical Scene Graph:** Modular character modeling (head, torso, hips, limbs, and facial details) connecting position, rotation, and scale transformation nodes.
* **Dynamic Kinematic Poses:** Composed matrix transformations (`tr.matmul`, multi-axis X/Y/Z rotations, and translations) defining distinct character postures.
* **3D Shader-Based Rendering:** Programmable pipeline with GLSL 330 core shaders (vertex and fragment) for rendering 3D geometries (`.off`).
* **Adaptive Cameras:** Dynamic configuration of view matrices (`lookAt`) and perspective projections designed to emphasize the drama of each pose.

##
* **Grafo de Escena Jerárquico:** Modelado modular del personaje (cabeza, torso, caderas, extremidades y detalles faciales) conectando nodos de posición, rotación y escalamiento.
* **Poses Cinemáticas Dinámicas:** Transformaciones matriciales compuestas (`tr.matmul`, rotaciones en ejes X/Y/Z y traslaciones) para definir las distintas posturas del personaje.
* **Renderizado 3D con Shaders:** Pipeline programable con shaders en GLSL 330 core (*vertex* y *fragment*) para la iluminación básica y renderizado de geometrías (`.off`).
* **Cámaras adaptativas:** Configuración dinámica de la matriz de vista (`lookAt`) y proyección perspectiva para resaltar la dramatismo de cada pose.



## Interactive Features
| <kbd>SPACE</kbd> | Cycles through 4 dramatic poses and adjusts the camera perspective for each scene. 
##
| <kbd>ESPACIO</kbd> | Alterna cíclicamente entre las 4 poses dramáticas y cambia la posición de la cámara según la escena. 
