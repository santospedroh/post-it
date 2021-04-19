from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

posts = [
{
    'author': 'Pedro Santos',
    'content': 'App Python Flask com acesso ao banco de dados MySQL. Aqui você pode deixar uma mensagem de texto. 🧑🏻‍💻 🚀 ',
    'date_posted': 'April 18, 2021'
},
{
    'author': 'Krobe Byrant',
    'content': 'Best Bastketballer of all times ',
    'date_posted': 'January 27, 2019'
},
{
    'author': 'Micheal Jordan',
    'content': 'As for this legend no  comments',
    'date_posted': 'January 27, 2019'
}
]

@app.route("/")
def home():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)