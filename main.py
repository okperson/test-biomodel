from flask import Flask
from flask_cors import CORS
from app.routes import *
from app.models import db
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'your_unique_secret_key'
# Cấu hình cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/minh/Downloads/biomodel-backend-master/instance/biomodel-browser.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {
    "origins": "127.0.0.2 5000", # Cho
    "methods": "*", # Các
    "allow_headers":"*"  
}},
supports_credentials= True)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Khởi tạo đối tượng SQLAlchemy với ứng dụng
db.init_app(app)

register_routes(app)
if __name__ == '__main__':
    app.run(debug=True)
    
