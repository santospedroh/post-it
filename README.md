# Post-it 📌

![build](https://github.com/santospedroh/post-it/actions/workflows/main_post-it-devopslab.yml/badge.svg) ![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=santospedroh_post-it&metric=alert_status) ![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=santospedroh_post-it&metric=security_rating)

## Sobre o projeto 💻

App Web simples para salvar mensagens em formato de post-it. O objetivo do projeto é reforçar os conhecimentos que foram aprendidos na disciplina DevOps Tools do curso DevOps Engineering and Cloud Solutions da Mackenzie.

Foi desenvolvido uma aplicação utilizando [Python](https://www.python.org/) e [Flask](https://flask.palletsprojects.com/en/1.1.x/). Também foi criada uma pipeline utilizando o [GitHub Actions](https://docs.github.com/en/actions) como ferramenta de CI para automatização dos teste unitários, testes de qualidade, testes funcionais, build e deploy nos ambientes de Homologação e Produção.

## Tecnologias utilizadas 👨‍💻

- [Git](https://git-scm.com)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLite3](https://www.sqlite.org/index.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Heroku](https://www.heroku.com/)
- [Azure](https://azure.microsoft.com/)
- [SonarCloud](https://sonarcloud.io/)

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
2. Abra o navegador web e acesse: <http://127.0.0.1:5000>
3. Pronto, aplicação executando!

---

Made with ♥ by Pedro Santos :wave: [Get in touch!](https://www.linkedin.com/in/santospedroh/)
