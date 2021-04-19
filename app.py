from flask import Flask, render_template, request
#from flask_wtf.csrf import CSRFProtect
from datetime import date
import sqlite3
import os

app = Flask(__name__)
#csrf = CSRFProtect(app)

exemple = [
{
    'nome': 'Pedro Santos',
    'mensagem': 'App Python Flask com acesso ao banco de dados MySQL. Aqui você pode deixar uma mensagem de texto. 🧑🏻‍💻 🚀 ',
    'criado_em': 'April 18, 2021'
}
]

def consult():
    # conexao
    conn = sqlite3.connect('post-it-database.db')
    conn.row_factory = sqlite3.Row
    curr = conn.cursor()
    # consulta
    curr.execute("SELECT nome, mensagem, datetime(criado_em,'localtime') as criado_em FROM post ORDER BY criado_em DESC")
    rows = curr.fetchall()
    return rows

def save(nome, mensagem):
    # conexao
    conn = sqlite3.connect('post-it-database.db')
    curr = conn.cursor()  
    #salva
    curr.execute("INSERT into post (nome, mensagem) values (?,?)",(nome,mensagem))  
    conn.commit()  

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "GET": 
        try:
            rows = consult()
            print("Efetuando consulta no SQLite.") 
            return render_template('index.html', posts = rows, show_modal=False )
        except Exception as e:
            print(e)
            return render_template('index.html', posts = exemple)

    if request.method == "POST":
        try:
            name = request.form["nome"]  
            message = request.form["mensagem"]  
            save(name, message, )
            print("Salvando dados no SQLite.") 
            
            rows = consult()
            return render_template('index.html', posts = rows, show_modal=True)         
        except Exception as e: 
            print(e)


if __name__ == '__main__':
    app.run(debug = True)