import rpyc
conn = rpyc.connect("localhost", 18861)

i = 1
while True:
    myfunc_async = rpyc.async_(conn.root.asyncadd)
    res = myfunc_async(1,2)
    print(res.ready)
    res.wait()

    if res.ready == True:
        x = conn.root.fetch_res(res.value)
        print(x)

    i = i + 1
    if i == 2:
        break

