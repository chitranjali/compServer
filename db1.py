import sqlite3
# conn = sqlite3.connect("sorted_res.db")
conn = sqlite3.connect("results.db")
c = conn.cursor()
sql_create_results_table = """ CREATE TABLE IF NOT EXISTS results (
                                            pid integer PRIMARY KEY AUTOINCREMENT,
                                            result integer,
                                            status text
                                        ); """

# sql_create_results_table = """ CREATE TABLE IF NOT EXISTS sorted_res (
#                                             pid integer PRIMARY KEY AUTOINCREMENT,
#                                             result text,
#                                             status text
#                                         ); """
# c.execute(sql_create_results_table)
# c.execute("INSERT INTO results (result, status) VALUES (5, 'processing')")
# c.execute("INSERT INTO results (result, status) VALUES (6, 'processing')")
# c.execute("INSERT INTO results (result, status) VALUES (7, 'processing')")

# c.execute("DELETE FROM results")

# c.execute("DROP TABLE results")
# conn.commit()
c.execute("SELECT * FROM results")
# c.execute("SELECT * FROM sorted_res")
print(c.fetchall())