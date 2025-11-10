# Space Invaders - Proyecto Comunitario

<div align="center">

![Space Invaders](assets/spaceship.png)

**Una versión moderna y de código abierto del clásico Space Invaders**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.1-green.svg)](https://pygame.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*¡Únete a la comunidad y ayuda a desarrollar el mejor Space Invaders de código abierto!*

</div>

## 🚀 Características Actuales

- ✅ Sistema de niveles progresivos
- ✅ Disparos y colisiones
- ✅ Enemigos con IA básica
- ✅ Sistema de vidas y puntuación
- ✅ Assets visuales personalizables
- ✅ Ejecutable para Windows, Linux y Mac

## 🎯 Roadmap y Mejoras Planeadas

¡Tu ayuda es necesaria para implementar estas características!

### Prioridad Alta
- [ ] Sistema de power-ups y bonificaciones
- [ ] Diferentes tipos de enemigos con comportamientos únicos
- [ ] Jefes finales por nivel
- [ ] Sistema de logros y estadísticas

### Prioridad Media
- [ ] Modo cooperativo (2 jugadores)
- [ ] Modo survival infinito
- [ ] Diferentes tipos de armas
- [ ] Escudos y barreras destructibles

### Prioridad Baja
- [ ] Modo historia con narrativa
- [ ] Editor de niveles
- [ ] Integración con líderes online
- [ ] Versión web con Pygame CE

## 🛠️ Comenzando

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/space-invaders-community.git
   cd space-invaders-community
   ```
2. **Crea un entorno virtual (recomendado)**
3. **Instala las dependencias**
4. **Ejecuta el código**

## 🎮 Controles

* **Flecha izquierda:** Mover nave a la izquierda
* **Flecha derecha:** Mover nave a la derecha
* **Espacio:** Disparar
* **R:** Reiniciar juego (cuando termina)
* **ESC:** Salir del juego

## 👥 Cómo Contribuir

¡Nos encanta recibir contribuciones! Hay muchas formas de ayudar:

### 🐛 Reportar Errores

Si encuentras un bug, por favor:

1. Revisa si ya existe un reporte en Issues
2. Si no existe, crea uno nuevo con:
	- Descripción clara del problema
	- Pasos para reproducirlo
	- Capturas de pantalla si es posible
  - Tu sistema operativo y versión de Python

### 💡 Sugerir Mejoras

¿Tienes una idea para mejorar el juego?

1. Ve a [Issues](https://github.com/develorian/My-Space-Invader/issues)
2. Crea un nuevo issue con la etiqueta "enhancement"
3. Describe tu idea en detalle

### 🔧 Contribuir con Código

1. Haz un fork del proyecto 
2. Crea una rama para tu feature

```bash
git checkout -b feature/nueva-caracteristica
```

3. Desarrolla tu feature
  - Sigue el estilo de código existente
  - Añade comentarios cuando sea necesario
  - Prueba tu código thoroughly
4. Haz commit de tus cambios

```bash
git commit -m "feat: añadir nueva característica X"
```
5. Push a la rama
```bash
git push origin feature/nueva-caracteristica
```
6. Abre un Pull Request

### 🎨 Contribuir con Arte y Assets
¿Eres artista? ¡Necesitamos tu ayuda!

- Sprites de naves enemigas
- Fondos espaciales
- Efectos de sonido
- Música de fondo
- Iconos y UI elements
Formato requerido: PNG para imágenes, WAV/OGG para sonidos.

## 🏗️ Estructura del Proyecto
```text
space-invaders-community/
├── main.py                # Punto de entrada del juego
├── game.py                # Lógica principal del juego
├── entities/              # Entidades del juego (naves, enemigos, etc.)
│   ├── player.py
│   ├── enemy.py
│   └── bullet.py
├── assets/                # Recursos del juego
│   ├── sprites/
│   ├── sounds/
│   └── fonts/
├── utils/                 # Utilidades y helpers
│   ├── constants.py
│   └── helpers.py
├── docs/                  # Documentación
├── tests/                 # Tests automatizados
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
```

## 🧪 Ejecutar Tests
```bash
# Ejecutar todos los tests
python -m pytest tests/

# Ejecutar tests con cobertura
python -m pytest tests/ --cov=.

# Ejecutar tests específicos
python -m pytest tests/test_player.py
```

## 📦 Crear Ejecutables

**Para Windows**
```bash
pyinstaller --onefile --windowed --name "SpaceInvaders" --add-data "assets;assets" main.py
```
**Para Linux**
```bash
pyinstaller --onefile --name "SpaceInvaders" --add-data "assets:assets" main.py
```
**Para MacOs**
```bash
pyinstaller --onefile --windowed --name "SpaceInvaders" --add-data "assets:assets" main.pypyinstaller --onefile --windowed --name "SpaceInvaders" --add-data "assets:assets" main.py
```

## 🎯 Áreas que Necesitan Ayuda

### Programación
- Optimización de rendimiento
- Implementación de nuevas mecánicas de juego
- Mejora de la IA enemiga
- Sistema de partículas y efectos visuales

### Arte y Diseño
- Diseño de sprites para nuevos enemigos
- Animaciones para naves y explosiones
- Diseño de interfaz de usuario
- Fondos parallax

### Sonido y Música
- Efectos de sonido para disparos y explosiones
- Música de fondo por niveles
- Efectos ambientales espaciales

### Documentación
- Mejorar este README
- Crear tutoriales para nuevos contribuyentes
- Documentar la API del juego

## 📝 Convenciones de Código
- Usamos **snake_case** para variables y funciones
- **PascalCase** para nombres de clases
- Comentarios en **inglés** (pero el código puede - estar en español)
- Commits siguiendo Conventional Commits

## 📜 Licencia
Este proyecto está bajo la GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007 - ver el archivo [LICENSE](https://github.com/develorian/My-Space-Invader/blob/main/LICENSE) para detalles.

## 🤝 Comunidad

- **Discord:** Únete a nuestro servidor

- **X (Ex-Twitter):** Síguenos para updates, en [🥷 ƬΉΣ DΣVΣᄂӨЯIΛП 🧑‍💻](https://x.com/develorian_https://x.com/develorian_) 

- **Reddit:** En nuestro Canal [r/pythonation](https://www.reddit.com/r/pythonation/)

- **Email:** thedevelorian@gmail.com

## 🙏 Agradecimientos
- A la comunidad de Pygame por las herramientas increíbles
- A los contribuyentes que han dedicado su tiempo
- A los testers que reportan bugs y sugieren mejoras

<div align="center">
¿Listo para unirte a la invasión? 🚀

"Solos podemos hacer poco, juntos podemos hacer mucho" - Helen Keller

https://img.shields.io/badge/Contribuye-Ahora!-brightgreen?style=for-the-badge

</div><div align="center">
¿Listo para unirte a la invasión? 🚀

"Solos podemos hacer poco, juntos podemos hacer mucho" - Helen Keller

https://img.shields.io/badge/Contribuye-Ahora!-brightgreen?style=for-the-badge

</div>

¿Preguntas? Revisa nuestras [FAQs](https://github.com/develorian/My-Space-Invader/issues/1) o abre un [issue](https://github.com/develorian/My-Space-Invader/issues).

## Estructura Final del Proyecto
```text
space-invaders-community/
├── README.md
├── main.py
├── game.py
├── build.py
├── requirements.txt
├── CONTRIBUTING.md
├── LICENSE
└── assets/
    ├── bullet.png
    ├── spaceship.png
    └── spaceship.ico
```