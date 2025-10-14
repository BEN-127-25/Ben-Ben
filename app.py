from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///da.db'
db = SQLAlchemy(app)

class myComms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<myComms {self.name}>'

@app.route('/')
def index():
    return render_template('index.html')
    return render_template('testing.html')
    









if __name__ == '__main__':
    app.run(debug=True)