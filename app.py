from colorama import Fore
import pyodbc



class trivia_game():
    def game_1(self):
        print(Fore.LIGHTBLUE_EX + '\n\t\t\t\t\t\t\t\t\t WELCOME TO TRIVIA GAME PLAYINGS \n' + Fore.RESET)
        user = int(input(Fore.LIGHTBLUE_EX + "\t\t\t\t\t\t\t\t\t Choose you want to the question>\n\n" + Fore.RESET +
                         Fore.LIGHTMAGENTA_EX + '\t\t 1.Enter for Python question\t\t' + Fore.RESET +
                         Fore.LIGHTYELLOW_EX + '2.Enter for General knowledge Question\n\n' + Fore.RESET +
                         Fore.LIGHTRED_EX + '\t\t\t\t\t\t\t\t 3.Enter for History Question \n' + Fore.RESET +
                         Fore.LIGHTYELLOW_EX + '\t\t 4.Enter for Civics Question \n' + Fore.RESET))
        if user == 1:
            Generals = pyodbc.connect('Driver={SQL Server};'
                                      'Server=LAPTOP-HGOMIVGU\MSSQLSERVER01;'
                                      'Database=Quiz;'
                                      'Trusted_Connection=yes;')

            X = 'SELECT Question,A,B,C,D ,Answer FROM dbo.Python_Questions'
            cursor = Generals.cursor()
            cursor.execute(X)
            score = 0
            for i in cursor:
                print(i[0])
                print("A", i[1], "\n", "B", i[2], "\n", "C", i[3], "\n", "D", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "Choose the best  answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/10")

        elif user == 2:
            Sports = pyodbc.connect('Driver={SQL Server};'
                                    'Server=LAPTOP-HGOMIVGU\MSSQLSERVER01;'
                                    'Database=Quiz;'
                                    'Trusted_Connection=yes;')

            Y = 'SELECT Question,A,B,C,D,Answer FROM dbo.Generalknowledge_Questions'
            cursor = Sports.cursor()
            cursor.execute(Y)
            score = 0
            for i in cursor:
                print(i[0])
                print(i[1], "\n", i[2], "\n", i[3], "\n", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/10")


        elif user == 3:
            Funny = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-HGOMIVGU\MSSQLSERVER01;'
                                   'Database=Quiz;'
                                   'Trusted_Connection=yes;')


            Z = 'SELECT Question,A,B,C,D,Answer FROM dbo.History_Questions'
            cursor = Funny.cursor()
            cursor.execute(Z)
            score = 0
            for i in cursor:
                print(i[0])
                print(i[1], "\n", i[2], "\n", i[3], "\n", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/10")

        elif user == 4:
            Funny = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-HGOMIVGU\MSSQLSERVER01;'
                                   'Database=Quiz;'
                                   'Trusted_Connection=yes;')

            Z = 'SELECT Question,A,B,C,D,Answer FROM dbo.History_Questions'
            cursor = Funny.cursor()
            cursor.execute(Z)
            score = 0
            for i in cursor:
                print(i[0])
                print(i[1], "\n", i[2], "\n", i[3], "\n", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/10")
        else:
            print("Thank you good by")
            exit()

# ben = trivia_game()
# ben.game_1()
