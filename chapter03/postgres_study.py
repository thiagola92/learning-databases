import psycopg2

database = psycopg2.connect("postgres://username:password@127.0.0.1")
cursor = database.cursor()

cursor.execute("""
  CREATE TABLE table_name(
    sku integer,
    name varchar(255),
    description text,
    category varchar(255)
  )
""")

cursor.execute("""
  INSERT INTO table_name
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis')
""")

cursor.execute("""
  UPDATE table_name
    SET name = 'super robô'
    WHERE sku = 134218478
""")

cursor.execute("""SELECT * FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
database.commit()
database.close()