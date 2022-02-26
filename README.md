# Computation Server

This is an implementation of computation server to support add(i, j), sort(arrayA) operations using synchronous, asynchronous and deferred synchronous RPCs.
For asynchronous RPC, the server immediately acknowledges an RPC call before it actually performs a computation.
The result of the computation is saved in a table on the server, which can be looked up by the client for the RPC result.
The design of the client will be slightly different from that in the synchronous RPC.
Instead of waiting for a synchronous RPC to return, the client using an asynchronous RPC switches to other computations and queries the server for the RPC result at a later time. 
For deferred synchronous RPC, the client w ill be interrupted to return the RPC result to the client when the server has completed its local computation.  

## Working

uses RPyC package for achieving the desired results.
The aysnc results are stored in sqlite db names results.

* Run the server with python server.py on port 18861
  ### Add:
      Tables: results.db
        * Synchronous: run sync_client.py, the function add() will be called with two p
          parameters, the clients keep waiting till it receives the result.
        * Asyncrhonous: run async_client_add.py, It connects to the server and calls the function
          asyncadd asynchronously by adding a wrapper from RPyC. The results are stored in a table
          on the server, and the client queries for the results after processing all tasks.
        * Deferred asynchronous: run defer_client.py, the client calls the functions with a callback 
          function as a parameter. The server process the results and interrupts the client as soon 
          as the result is ready with the callback function
  ### Sort:
      Tables: sorted_res
        * Synchronous: run sync_client_sort.py, the function will pass the array as parameter, and 
          server processes the result and sends back to client.
        * Asyncrhonous: run async_client_sort.py, It connects to the server and calls the function
          asyncadd asynchronously by adding a wrapper from RPyC. The results are stored in a table
          on the server, and the client queries for the results after processing all tasks. The sor
          ted array is stored in stringified format in the db coloumn.
        * Deferred asynchronous: run defer_client_sort.py, the client calls the functions with a callback 
          function as a parameter. The server process the results and interrupts the client as soon 
          as the result is ready with the callback function


