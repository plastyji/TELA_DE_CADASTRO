import sqlite3 as db
from tkinter import messagebox


def connectionDB():
    conn = db.connect('school.db')
    return conn


def register_studant(name, cpf , date_born, name_mother, phone,email):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT cpf FROM Alunos
            WHERE cpf = ?''',(cpf,))
        CPF_REGISTER = cursor.fetchone()
        if CPF_REGISTER:
            conn.close()
            return False, "O aluno ja é cadastrado"
        cursor.execute('''INSERT INTO Student (cpf, name, date_born, name_mother, email, phone) values (?,?,?,?,?,?)''',(cpf, name, date_born,name_mother,email,phone))
        conn.commit()
        conn.close()
        return True, "O aluno foi cadastrado com sucesso"

    except Exception as e:
        conn.close()
        return False, f"ERRO AO CADASTRAR O ALUNO. ERRO {str(e)}"


def register_teacher(name, cpf, date_born, name_mother, phone, email):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT cpf FROM teacher
            WHERE cpf = ?''', (cpf,))
        CPF_REGISTER = cursor.fetchone()
        if CPF_REGISTER:
            conn.close()
            return False, "O professor ja é cadastrado"
        cursor.execute('''INSERT INTO teacher (cpf, name, date_born, name_mother, email, phone) values (?,?,?,?,?,?)''',
                       (cpf, name, date_born, name_mother, email, phone))
        conn.commit()
        conn.close()
        return True, "O professor foi cadastrado com sucesso"

    except Exception as e:
        conn.close()
        return False, f"ERRO AO CADASTRAR O PROFESSOR. ERRO {str(e)}"

def register_course(name_course, shift, duration):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute(''' INSERT INTO course(name_course, shift, duration) values (?,?,?)
                        ''',(name_course, shift, duration))
        conn.commit()
        conn.close()
        return True, "Curso cadastrado corretamente"
    except Exception as e:
        conn.close()
        return False,  f'Erro ao cadastrar curso. Erro: {str(e)}'

def register_class(id_course, cpf_teacher):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute('''select id from course where id=?''', (id_course,))
        course  =  cursor.fetchone()
        cursor.execute(''' select cpf from teacher where cpf=?''',(cpf_teacher))
        teacher = cursor.fetchone()
        if not(course and teacher):

            conn.close()
            return False, "Curso ou Professor não existe" \
        cursor.execute(''' INSERT INTO class(id_course, cpf_teacher ) value (?,?)''', (id_course, cpf_teacher))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        return False, f'Erro ao cadastrar a turma. ERRO{str(e)}'


    except: