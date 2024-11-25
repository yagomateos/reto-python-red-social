# Red Social Python y Flask

Una red social simple desarrollada con Python y Flask, que permite a los usuarios crear perfiles, publicar mensajes, seguir a otros usuarios y más.

## 🚀 Características

- 👤 Creación de perfiles de usuario
- 📝 Publicación de posts
- 👥 Sistema de seguidores
- ❤️ Sistema de likes
- 💬 Comentarios en posts
- 📱 Interfaz web responsive

## 🛠️ Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Un editor de código (recomendado: Visual Studio Code)

## ⚙️ Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/yagomateos/reto-python-red-social.git
cd reto-python-red-social
```

2. **Crear un entorno virtual**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install flask
```

## 🚀 Ejecutar la aplicación

1. **Activar el entorno virtual** (si no está activado)
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Ejecutar la aplicación**
```bash
python app.py
```

3. **Acceder a la aplicación**
- Abre tu navegador
- Visita `http://localhost:5000`

## 📁 Estructura del Proyecto

```
reto-python-red-social/
├── venv/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   └── profile.html
├── app.py
├── social_network.py
└── README.md
```

## 💻 Uso

1. **Página Principal**
   - Ver todos los posts
   - Crear nuevos posts
   - Ver lista de usuarios

2. **Perfil de Usuario**
   - Ver información del usuario
   - Ver posts del usuario
   - Seguir/dejar de seguir usuarios

3. **Interacción**
   - Crear posts
   - Dar like a posts
   - Comentar en posts
   - Seguir a otros usuarios

## 🔧 Solución de Problemas Comunes

### Error: "No module named 'flask'"
```bash
pip install flask
```

### Error: "No se puede activar el entorno virtual"
- Asegúrate de estar en el directorio correcto
- Verifica que Python está instalado correctamente
- Intenta recrear el entorno virtual

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👥 Autor

- [@yagomateos](https://github.com/yagomateos)

## 🙏 Agradecimientos

- Inspirado en redes sociales modernas
- Desarrollado como proyecto de aprendizaje
- Gracias a la comunidad de Python y Flask

---
⌨️ con ❤️ por [Yago Mateos](https://github.com/yagomateos)