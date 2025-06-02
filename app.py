from flask import Flask, render_template, request, redirect, url_for
from db import conectar

app = Flask(__name__)

@app.route('/')
def index():
    conexao = conectar()
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT a.id, a.nome, a.matricula, t.nome AS turma
                FROM tb_aluno a
                LEFT JOIN tb_turma t ON a.id_tb_turma = t.id
            """)
            alunos = cursor.fetchall()

            cursor.execute("SELECT * FROM tb_turma")
            turmas = cursor.fetchall()
    return render_template('index.html', alunos=alunos, turmas=turmas)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form['nome']
    matricula = request.form['matricula']
    turma = request.form['turma']
    conexao = conectar()
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tb_aluno (nome, matricula, id_tb_turma) VALUES (%s, %s, %s)",
                (nome, matricula, turma)
            )
            conexao.commit()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    conexao = conectar()
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM tb_aluno WHERE id = %s", (id,))
            conexao.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
