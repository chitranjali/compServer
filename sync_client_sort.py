import rpyc
conn = rpyc.connect("localhost", 18861)

y = conn.root.sort([5, 3, 7])
print(y)