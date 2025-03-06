# WorkShop-1
# Descripción

Este proyecto consiste en migrar datos desde un archivo CSV a una base de datos MySQL, realizar análisis sobre estos datos y generar visualizaciones interactivas en un dashboard.

# Tecnologías Utilizadas

Python 🐍

MySQL 🛢️

Pandas 📊

SQLAlchemy 🔗

Streamlit 🌐

Plotly 📈

dotenv 🔒

# Instalación

1️⃣ Clona el repositorio:

git clone https://github.com/KevinMG1601/WorkShop-1.git
cd proyecto

2️⃣ Instala las dependencias:

pip install -r requirements.txt

3️⃣ Crea el archivo .env y agrega tus credenciales de MySQL:

DB_USER = "USER"
DB_PASSWORD = "PASSWORD"
DB_HOST = "localhost"
DB = "Database"

4️⃣ Ejecuta el script para migrar los datos desde el CSV a MySQL:

En la carpeta jupyter esta los dos notebooks el primero seria el de limpieza y luego el de migration.

5️⃣ Corre el dashboard en Streamlit:

cd dashboard
streamlit run dashboard.py

