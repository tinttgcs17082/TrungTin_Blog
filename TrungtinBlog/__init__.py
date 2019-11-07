from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6ee238677970bd0480913746877f36b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'    

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER']= 'smtp.live.com'
app.config['MAIL_PORT ']= 25
app.config['MAIL_USERNAME'] = 'a00.n0reply@hotmail.com'
app.config['MAIL_PASSWORD'] = 'tinpro123'
mail = Mail(app)

from TrungtinBlog.users.routes import users
from TrungtinBlog.posts.routes import posts
from TrungtinBlog.main.routes import main
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
