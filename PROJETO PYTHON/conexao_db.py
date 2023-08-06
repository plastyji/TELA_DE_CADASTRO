import sqlite3 as db

def connectionDB():
    conn = db.connect("school.db")
    return conn
def create_table_stud(conn):
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student(
            cpf INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            date_born TEXT NOT NULL, 
            name_mother TEXT NOT NULL,
            email TEXT NOT NULL, 
            phone TEXT NOT NULL
            )   
    ''')
def create_table_teacher(conn):
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS teacher(
                cpf INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                date_born TEXT NOT NULL, 
                name_mother TEXT NOT NULL,
                email TEXT NOT NULL, 
                phone TEXT NOT NULL
            )  
       ''')
def create_table_course(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_course TEXT NOT NULL,
            shift TEXT NOT NULL,
            duration TEXT NOT NULL       
        )
    ''')
def create_table_class(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Class(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_course INTEGER , 
            cpf_teacher INTEGER,
            FOREIGN KEY(id_course) REFERENCES Course(id)
            FOREIGN KEY(cpf_teacher) REFERENCES teacher(cpf)                   
        )
    ''')
def create_table_studant_class(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Studant_Class(
            id_studant INTEGER,
            id_class INTEGER,
            FOREIGN KEY(id_studant) REFERENCES Studant(id) 
            FOREIGN KEY(id_class) REFERENCES Class(id) 
        )
    ''')



if __name__ == "__main__":
    conn = connectionDB()
    create_table_stud(conn)
    create_table_teacher(conn)
    create_table_course(conn)
    create_table_class(conn)
    create_table_studant_class(conn)
    
    #conn.close()

def insert():
    conn = connectionDB()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Course(name_course, shift, duration) VALUES
        ('DFS', 'Manhã', '12 Meses')

    ''')
    print("inserido com sucesso ")
    conn.commit()



def seach():
    conn = connectionDB()
    cursor = conn.cursor()
    cursor.execute("select * from student")
    result = cursor.fetchall()
    for lista in result:
        print(lista)

seach()
