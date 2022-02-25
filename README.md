# Computation Server

This is an implementation of computation server to support add(i, j), sort(arrayA) operations using synchronous, asynchronous and deferred synchronous RPCs.
For asynchronous RPC, the server immediately acknowledges an RPC call before it actually performs a computation.
The result of the computation is saved in a table on the server, which can be looked up by the client for the RPC result.
The design of the client will be slightly different from that in the synchronous RPC.
Instead of waiting for a synchronous RPC to return, the client using an asynchronous RPC switches to other computations and queries the server for the RPC result at a later time. 
For deferred synchronous RPC, the client will be interrupted to return the RPC result to the client when the server has completed its local computation.  

## Working

uses RPyC package for achieving the desired results.
The aysnc results are stored in sqlite db names results.


