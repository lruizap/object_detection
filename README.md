# Proyecto de Detección de Objetos

## Descripción

Este proyecto tiene como objetivo desarrollar un sistema de detección de objetos utilizando técnicas de aprendizaje automático y procesamiento de imágenes.

El proyecto incluye la recolección de imágenes de objetos específicos, la preparación de los datos, el entrenamiento de un modelo de detección de objetos y su evaluación en un conjunto de prueba.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)

## Características

- Creación del dataset.
- Organización automática de imágenes en conjuntos de entrenamiento y prueba.
- Implementación de modelos de detección de objetos.
- Evaluación del rendimiento del modelo.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.6 o superior
- Bibliotecas necesarias:
  - Todas se encuentran en el fichero `requirements.txt`
  
Puedes instalar las bibliotecas requeridas utilizando pip:

```bash
pip install -r requirements.txt
```

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/lruizap/object_detection.git
   cd tu_repositorio
   ```

2. **Instala las librerías**:

Puedes instalar las bibliotecas requeridas utilizando pip:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```markdown
/object_detect
│
├── dataset
│   ├── train
│   ├── test
│   ├── organizeImages.py
│   └── downloadImages.py
├── public
│   ├── img
│   └── zip
├── README.md
└── requirements.txt
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza los cambios y haz commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.
