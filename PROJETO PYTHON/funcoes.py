import sqlite3 as db
from tkinter import messagebox


def connectionDB():
    conn = db.connect('school.db')

    return conn


def register_student(name, cpf, date_born, name_mother, phone, email):
    conn = connectionDB()
    cursor = conn.cursor()
    try:

        cursor.execute('''SELECT cpf FROM student
            WHERE cpf = ?''', (cpf,))
        CPF_REGISTER = cursor.fetchone()

        if CPF_REGISTER:
            conn.close()
            return False, "O aluno ja é cadastrado"
        cursor.execute('''INSERT INTO Student (cpf, name, date_born, name_mother, email, phone) values (?,?,?,?,?,?)''',(cpf, name, date_born, name_mother,email,phone))
        print("ok")
        conn.commit()
        conn.close()
        messagebox.showinfo(title="Sucesso", message="Sucesso ao cadastrar o Estudante")
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
        course = cursor.fetchone()
        cursor.execute(''' select cpf from teacher where cpf=?''',(cpf_teacher))
        teacher = cursor.fetchone()
        if not(course and teacher):

            conn.close()
            return False, "Curso ou Professor não existe"
        cursor.execute(''' INSERT INTO class(id_course, cpf_teacher ) value (?,?)''', (id_course, cpf_teacher))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        return False, f'Erro ao cadastrar a turma. ERRO{str(e)}'

def register_student_class(id_studant, id_class):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute("Select cpf from student where cpf = ?", (id_studant,))
        student_exist = cursor.fetchone()

        cursor.execute("Select id from class where id = ?", (id_class,))
        class_exist = cursor.fetchone()

        if not (student_exist, class_exist):
            return False , "Aluno ou turma não encontrado."
        cursor.execute('''INSERT INTO Studant_Class(id_studant, id_class)
        values (?, ?)''', (id_studant, id_class))
        conn.commit()
        return True, "Aluno cadastrado na turma com sucesso."

    except Exception as e:
        return False, f"Erro ao cadastrar aluno na turma: {str(e)}"
    finally:
        conn.close()

def view_student():
    conn = connectionDB()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM Student
    ''')
    student = cursor.fetchall()
    conn.close()

    return student


def view_teacher():
    conn = connectionDB()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM teacher
    ''')
    teacher = cursor.fetchall()
    conn.close()

    return teacher

def view_course():
    conn = connectionDB()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM Course
    ''')
    Couser = cursor.fetchall()
    conn.close()

    return Couser
def view_class():
    conn = connectionDB()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM Class
    ''')
    clas = cursor.fetchall()
    conn.close()
    return clas

#Atualização#
def atualization_people(name, cpf, date_born, name_mother, phone, email):
    conn = connectionDB()
    cursor = conn.cursor()

    try:
        cursor.execute(''' SELECT cpf FROM Student where cpf = ?''', (cpf,))
        student_exist = cursor.fetchone()
        cursor.execute(''' SELECT cpf FROM teacher where cpf = ?''', (cpf,))
        teacher_exist = cursor.fetchone()

        if not (student_exist or teacher_exist):
            return False, "Cpf não encontrado"

        if(student_exist):
            cursor.execute('''
                    UPDATE student SET name = ? , cpf = ?,
                    date_born = ? , name_mother = ? , phone = ? , email = ? WHERE cpf = ?
            ''', (name, cpf, date_born, name_mother, phone, email,cpf))

        elif(teacher_exist):
            cursor.execute('''
                                UPDATE teacher SET name = ? , cpf = ?,
                                date_born = ? , name_mother = ? , phone = ? , email = ? WHERE cpf = ?
                        ''', (name, cpf, date_born, name_mother, phone, email, cpf))
        conn.commit()


        return True, "Pessoa Atualizada Com Sucesso"
    except Exception as e:

        return  False, f'Erro ao atualizar pessoa. {str(e)}'
    finally:
        conn.close()


def delete_people(cpf):
    conn = connectionDB()
    cursor = conn.cursor()
    try:
        cursor.execute(''' SELECT cpf FROM Student where cpf = ?''', (cpf,))
        student_exist = cursor.fetchone()
        cursor.execute(''' SELECT cpf FROM teacher where cpf = ?''', (cpf,))
        teacher_exist = cursor.fetchone()

        if not (student_exist or teacher_exist):
            return False, "Cpf não encontrado"
        if(student_exist):
            cursor.execute('DELETE FROM Student where cpf = ?'(cpf,))

        elif(teacher_exist):
            cursor.execute('DELETE FROM teacher where cpf = ? '(cpf,))

        conn.commit()

        return True, "Pessoa Excluida Com Sucesso"
    except Exception as e:
        return False, f"Erro ao excluir pessoa.{str(e)} "
    finally:
        conn.close()

