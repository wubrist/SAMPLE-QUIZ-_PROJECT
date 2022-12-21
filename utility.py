import pyodbc


def table():
    connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL '
                             "Server};SERVER=LAPTOP-HGOMIVGU\MSSQLSERVER01;"
                             'Database=Quiz;'
                             'Trusted_Connection=yes;')

    # query = "CREATE TABLE [Python_Questions](ID_Number int primary key, Question varchar(200), A varchar(50), B varchar(50), " \
    #         "C varchar(50), D varchar(50), Answer varchar(50)) "
    # cursor = connect.cursor()
    # cursor.execute(query)
    # connect.commit()

    # query = "CREATE TABLE Generalknowledge_Questions(ID_Number int primary key, Question varchar(200), A varchar(50), B varchar(50), " \
    #         "C varchar(50), D varchar(50), Answer varchar(50)) "
    # cursor = connect.cursor()
    # cursor.execute(query)
    # connect.commit()

    # query = "CREATE TABLE History_Questions(ID_Number int primary key, Question varchar(200), A varchar(50), B varchar(50), " \
    #         "C varchar(50), D varchar(50), Answer varchar(50)) "
    # cursor = connect.cursor()
    # cursor.execute(query)
    # connect.commit()

    query = "CREATE TABLE Civics_Questions(ID_Number int primary key, Question varchar(200), A varchar(50), B varchar(50), " \
            "C varchar(50), D varchar(50), Answer varchar(50)) "
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()

table()


def question_input():
    connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL '
                             "Server};SERVER=LAPTOP-HGOMIVGU\MSSQLSERVER01;"
                             'Database=Quiz;'
                             'Trusted_Connection=yes;')
    cursor = connect.cursor()

    ID_Number = input("id_number  ")
    Question1 = input("Question:?  ")
    A = input("Choice A : ")
    B = input("Choice B : ")
    C = input("Choice C  :")
    D = input("Choice D  :")
    Answer = input("The answer is : ")
    cursor.execute("INSERT Civics_Questions(ID_Number,Question,A,B,C,D,Answer)"
                   "VALUES(?,?,?,?,?,?,?)", (ID_Number, Question1, A, B, C, D, Answer))
    connect.commit()


question_input()
