# from dotenv import load_dotenv
# from os import getenv
# import psycopg2

# # load .env file
# load_dotenv()

# #create a class
# class PGSQL:
#     __user = getenv("week5")
#     __password = getenv("Redrum05")
#     __server = getenv("Server")
#     __pg_con = psycopg2.connect(
#         dbname=__user,
#         user=__user,
#         password=__password,
#         host=__server
#     )
#     __cur = __pg_con.cursor()

# pg = PGSQL()
# print(PGSQL.__user)

# # creating a static method 
# @staticmethod
# def create_file(filepath : str):
#     """Open a file by the filepath and apply it to an SQL Table"""
#     with open(filepath, 'r') as f:
#         sql_file = f.read()
#         return sql_file