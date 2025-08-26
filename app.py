from flask import Flask
from flask_mysqldb import MySQL
import os
from models import DB_NAME
from routes import configure_routes




app = Flask(__name__)
app.secret_key = "your-secret-key"

# Upload folder config
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rachel_sql17'
app.config['MYSQL_DB'] = 'faith_db'

mysql = MySQL(app)

# Import routes after app + mysql are ready
configure_routes(app, mysql)

if __name__ == "__main__":
    app.run(debug=True)
