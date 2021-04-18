from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def home():
    return "Olá Mundo!"

if __name__ == '__main__':
    app.run(debug=True)