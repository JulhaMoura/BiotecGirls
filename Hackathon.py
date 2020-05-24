import sqlite3
conn = sqlite3.connect('estudantes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
UserID VARCHAR(20) NOT NULL,
username VARCHAR(60) NOT NULL,
firstname VARCHAR(60) NOT NULL,
email VARCHAR(60) NOT NULL,
password VARCHAR(80) NOT NULL);
''')

#gravando no bd
conn.commit()

#solicitando dados
p_1 = input('UserID: ')
p_2 = input('username: ')
p_3 = input('firstname: ')
p_4 = input('email: ')
p_5 = input('password: ')

#inserindo informações
cursor.execute('''
INSERT INTO students(UserID, username, firstname, password)
VALUES(?,?,?,?)
''', (p_1, p_2, p_3, p_4, p_5))

print('Dados inseridos com sucesso!!!')

#gravando no bd
conn.commit()

#verificando inversão
#lendo os dados
cursor.execute("""
SELECT*FROM students;
""")
print('lendo dados inseridos')

for linha in cursor.fetchall():
    print(linha)

cursor.close()

