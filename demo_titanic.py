import pandas as pd
import psycopg2

df = pd.read_csv(r'https://raw.githubusercontent.com/lucchesia7/coding-temple-da-sql-day-1/main/day_1/data/titanic.csv')
connection = 'postgres://dcneuqia:MF2C-f0UCNs0YQ-iRa6bnPs60MXyanIA@rajje.db.elephantsql.com/dcneuqia'
df.to.sql("titanic", con=connection)
display(pd.read_sql_table("titanic", con=connection))
print(df)

# for value in range(len(df)):
#     cur.execute(f"""INSERT INTO titanic(index, survived, ) VALUES({df['Survived'][value]})""")

#    df.to_sql('titanic') 

# conn.commit()
# cur.close()
# conn.closer()
