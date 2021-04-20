# Post-it 📌

[workflow](https://github.com/santospedroh/post-it/actions/workflows/main_post-it-devopslab.yml/badge.svg)

## Sobre o projeto 💻

Um App Web simples para salvar mensagens online. O objetivo do projeto é estudar e reforçar os conhecimentos do curso DevOps Engineering and Cloud Solutions da Mackenzie.

## Tecnologias usadas 👨‍💻

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLite3](https://www.sqlite.org/index.html)

## Instalação 🛠

Você vai precisar do [Git](https://git-scm.com) instalado em seu computador para clonar o projeto os demais passo estão descritos abaixo.

### Clonando o projeto

```bash
# Clone this repository
$ git clone git@github.com:santospedroh/post-it.git

```

### Python 3

1. Vá ao site <https://www.python.org/downloads/>;
2. Escolha a versão que deseja de acordo com o seu Sistema Operacional;
3. Prossiga no processo de instalação.

### Dependências do Python 3

1. Flask: `pip install flask`
2. Flask Wtf: `pip install flask_wtf`
3. Pytest: `pip install pytest`
4. Coverage: `pip install coverage`
5. Sqlite3: `pip install sqlite`

### Criando banco de dados SQLite

O SQLite é um banco de dados em arquivo, nesse projeto o arquivo de banco de dados é o : `post-it-database.db`. Esse arquivo já vem com 3 registros e já pode ser utilizado.

Se você precisar criar um banco de dados novo siga as instruções abaixo no terminal:

```bash

# Create database project Post-it
$ cd schema
$ python3 create_db.py
Banco de daos criado com sucesso.
$ python3 create_table.py
Tabela criada com sucesso.
$ python3 insert_data.py
Dados inseridos com sucesso.

```
Você precisa mover o arquivos `post-it-database.db` para o diretório raiz do projeto.

## Executando 🚀

### Start App 

1. Para executar o projeto digite no terminal : $ `python3 app.py`	
2. Abra o navegador web e acesse: <http://localhost:5000>
3. Pronto, aplicação executando!


---

Made with ♥ by Pedro Santos :wave: [Get in touch!](https://www.linkedin.com/in/santospedroh/)
