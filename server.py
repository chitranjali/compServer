import time
import rpyc
import sqlite3

class MyService(rpyc.Service):
    def __init__(self):
        # connect to results db
        self._conn = sqlite3.connect("results.db")
        self._cursor = self._conn.cursor()

    def insert_res(self, record):
        with self._conn:
            self._cursor.execute("replace into results (result, status) values (?, ?)",
                      (record["result"], record["status"]))
            print(self._cursor.lastrowid)
            return self._cursor.lastrowid

    def update_res(self, record):
        sql = ''' UPDATE results
                      SET result = ? ,
                          status = ?
                      WHERE pid = ?'''
        with self._conn:
            self._cursor.execute(sql, (record["result"], record["status"], record["pid"]))
            return self._cursor.lastrowid

    def exposed_fetch_res(self, pid):
        '''
        This will let the client fetch the status of a async request
        :param pid:
        :return:
        '''
        sql = ''' SELECT pid, result, status FROM results
                      WHERE pid = ?'''
        with self._conn:
            self._cursor.execute(sql, (pid,))
            result = self._cursor.fetchall()
            return result

    def exposed_add(self, i, j):
        return i + j

    def exposed_asyncadd(self, i, j):
        record = {}

        print("Adding rec to table")
        record["result"] = 0
        record["status"] = "Processing"
        row_id = self.insert_res(record)

        time.sleep(5)
        added_res = i + j

        record = {}
        record["pid"] = row_id
        record["result"] = added_res
        record["status"] = "Completed"
        row_id = self.update_res(record)
        return row_id

    def exposed_deferadd(self, i, j, callback):
        '''
        This method will send the result back to client as soon as processing completes, an example for
        deferred aync callback
        :param i:
        :param j:
        :param callback:
        :return:
        '''
        self.callback = rpyc.async_(callback)
        time.sleep(5)
        k = i + j
        self.callback(k)

    def exposed_sorta(self, A):
        return sorted(A)

t = rpyc.ThreadedServer(MyService, port=18861)
t.start()