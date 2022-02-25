import sqlite3

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE  animal_colors(" \
        "animal_id INT," \
        "color_id INT)"
cursor.execute(query)
con.close()
