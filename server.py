import time
import rpyc
import sqlite3

class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.connection.commit()
        return self._cursor.lastrowid

    def insert_res(self, record, table):
        sql = "replace into {}  (result, status) values (?, ?)".format(table)
        row_id = self.execute(sql, (record["result"], record["status"]))
        return row_id

    def update_res(self, record, table):
        sql = "UPDATE {} SET result = ? , status = ? WHERE pid = ?".format(table)
        row_id = self.execute(sql, (record["result"], record["status"], record["pid"]))
        return row_id

    def fetch_res(self, pid, table):
        sql = "SELECT pid, result, status FROM {} WHERE pid = ?".format(table)
        self.execute(sql, (pid,))
        result = self._cursor.fetchall()
        return result

class MyService(rpyc.Service):
    def exposed_add(self, i, j):
        return i + j

    def exposed_asyncadd(self, i, j):
        db = Database("results.db")
        record = {}

        print("Adding rec to table")
        record["result"] = 0
        record["status"] = "Processing"
        row_id = db.insert_res(record, "results")

        time.sleep(5)
        added_res = i + j

        record = {}
        record["pid"] = row_id
        record["result"] = added_res
        record["status"] = "Completed"
        row_id = db.update_res(record, "results")
        return row_id

    def exposed_deferadd(self, i, j, callback):
        self.callback = rpyc.async_(callback)
        time.sleep(5)
        k = i + j
        self.callback(k)

    def exposed_sort(self, A):
        return sorted(A)

    def exposed_asyncsort(self, t):
        record = {}

        db = Database("sorted_res.db")
        print("Adding rec to table")
        record["result"] = ""
        record["status"] = "Processing"
        row_id = db.insert_res(record, "sorted_res")

        time.sleep(5)
        unsorted_list = list(t)
        sorted_res = sorted(unsorted_list)
        res = ','.join(map(str, sorted_res))

        record = {}
        record["pid"] = row_id
        record["result"] = res
        record["status"] = "Completed"
        row_id = db.update_res(record, "sorted_res")
        return row_id

    def exposed_defersort(self, a, callback):
        self.callback = rpyc.async_(callback)
        time.sleep(5)
        sorted_res = sorted(a)
        self.callback(sorted_res)

    def exposed_fetch_res(self, pid, db, table):
        db = Database(db)
        res = db.fetch_res(pid, table)
        return res

t = rpyc.ThreadedServer(MyService, port=18861)
t.start()