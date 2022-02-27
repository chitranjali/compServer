import sqlite3
conn = sqlite3.connect("sorted_res.db")
c = conn.cursor()
sql_create_results_table = """ CREATE TABLE IF NOT EXISTS sorted_res (
                                            pid integer PRIMARY KEY AUTOINCREMENT,
                                            result text,
                                            status text
                                        ); """
c.execute(sql_create_results_table)
# conn.commit()
c.execute("SELECT * FROM sorted_res")
print(c.fetchall())