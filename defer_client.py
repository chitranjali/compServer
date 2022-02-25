import rpyc
conn = rpyc.connect("localhost", 18861)

def result(k):
    print("Result is {}".format(k))

myfunc_defer = conn.root.deferadd
res = myfunc_defer(1, 2, result)
