import rpyc
conn = rpyc.connect("localhost", 18861)

i = 1
result_ids = []
while True:
    myfunc_async = rpyc.async_(conn.root.asyncadd)
    res = myfunc_async(1, 2)
    result_ids.append(res)
    # print(result_ids)
    i = i + 1
    if i == 5:
        break

#Print the status of results
for x in result_ids:
    if x.ready == True:
        rec = conn.root.fetch_res(x.value, "results.db", "results")
        print(rec)
    else:
        res.wait()
        continue


