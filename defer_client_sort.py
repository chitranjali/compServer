import rpyc
conn = rpyc.connect("localhost", 18861)

def result(k):
    print(k)

myfunc_defer = conn.root.defersort
res = myfunc_defer([3, 1, 2], result)
