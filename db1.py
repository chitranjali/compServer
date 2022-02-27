import sqlite3
# conn = sqlite3.connect("sorted_res.db")
conn = sqlite3.connect("results.db")
c = conn.cursor()
sql_create_results_table = """ CREATE TABLE IF NOT EXISTS results (
                                            pid integer PRIMARY KEY AUTOINCREMENT,
                                            result integer,
                                            status text
                                        ); """

c.execute(sql_create_results_table)

c.execute("SELECT * FROM results")
print(c.fetchall())