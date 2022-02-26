import rpyc
conn = rpyc.connect("localhost", 18861)

i = 1
while True:
    x = conn.root.add(4, 7)
    print(x)
    i = i + 1
    if i == 5:
        break
    # assert x == 11
