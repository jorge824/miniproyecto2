# Control de Dedos con Arduino 🖐️➡️🕹️
Sistema que detecta la cantidad de dedos levantados en tiempo real usando visión por computadora y envía el resultado a un Arduino mediante comunicación serial.

![Demo Conceptual](docs/demo-concept.png) *(Recomendado: añadir GIF/video demo)*

## Características Principales ✨
- Detección de manos en tiempo real con MediaPipe
- Conteo de dedos levantados
- Comunicación serial con Arduino
- Visualización con OpenCV
- Fácil integración con proyectos de robótica/IoT

## Requisitos de Hardware 🛠️
- Cámara web
- Placa Arduino (Uno, Nano, Mega, etc.)
- Cable USB para Arduino
- Computadora con puertos USB disponibles

## Instalación ⚙️

### Dependencias
```bash
# Crear y activar entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows

# Instalar dependencias
pip install opencv-python mediapipe pyserial
