'''
CONNECTION Python - PostgreSQL
Powered by > GABRIEL CARVALHO
Github > GabPhoenix
'''

# IMPORTING MODULE
try:
    import psycopg2
except ImportWarning:
    print("You haven't this module installed. \n Please install now!")
except ImportError:
    print("An error occourred while importing the module psycopg2 \n please verify the installation!")

'''
CONNECTION FUNCTION IS TO START THE CONNECTION WITH 
POSTGRESQL, CALL IT FIRST!
'''
def connection():
    try:
        # CONNECTION
        global con, cur
        con = psycopg2.connect(host="localhost", 
        database="postgres", 
        user="YOUR USER HERE", 
        password="YOUR PASSWORD HERE")
        cur = con.cursor() #CREATING A CURSOR
        print("SUCCESFULLY CONNECTED!")
    except psycopg2.DatabaseError:
        print("IMPOSSIBLE CONNECT WITH SERVER!")
        return False


# RUN FUNCITION IS TO RUN SQL COMMANDS 
def runCommand(sql):
    try:
        cur.execute(sql)
        con.commit()
    except psycopg2.DatabaseError:
        print("IMPOSSIBLE RUN COMMAND")
        return False


# READ FUNCTION IS TO RUN AND RECIVE WITH SQL COMMANDS
def read(sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except psycopg2.DatabaseError:
        print("IMPOSSIBLE READ, PLEASE VERIFY THE COMMAND")
        return False


'''
WARNING: NEVER forget to call close function after connect 
with the server!
''' 
def closeFunction():
    try:
        cur.close()
        con.close()
    except psycopg2.DatabaseError:
        print("IMPOSSIBLE CLOSE, PLEASE VEFIFY THE CONNECTION")
        return False