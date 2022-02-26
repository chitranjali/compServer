import rpyc

conn = rpyc.connect("localhost", 18861)

result_ids = []

myfunc_async = rpyc.async_(conn.root.asyncsort)
a = [8, 9, 7]
t = tuple(a)
res = myfunc_async(t)
result_ids.append(res)
res.wait()

#Print the status of results
for x in result_ids:
    if x.ready == True:
        rec = conn.root.fetch_res(x.value, "sorted_res.db", "sorted_res")
        print(rec)
    else:
        res.wait()
        continue

