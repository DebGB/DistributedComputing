# DistributedComputing
Consider a scenario featuring a single server (Server), two user nodes (User1 and User 2), and three content providers (Content Provider1, Content Provider2, and Content Provider3). Please note the following:
a)	The arrangement of the content providers, user nodes and the server is illustrated below.
b)	Content providers produce text files intended for storage on the server.
o	Content provider 1 in Node 1 produces text files to be stored in Node 2 – Server
o	Content provider 2 in Node 2 produces text files similarly for Node 2: Server to store
o	Same for CP3
c)	User nodes have simultaneous read access to the server contents. However, for writing file contents onto the server, distributed mutual exclusion is necessary. Since it is a distributed environment, conventional locks are ineffective. Message passing techniques, as discussed in class videos, should be utilized. Additionally, the implementation should incorporate the concept of multithreading.
o	
d)	It is possible for multiple content providers to generate identical files. To address this, at the server side, duplicate files should be identified and only one instance of each file should be retained. Utilizing hashing techniques is recommended for efficiently detecting duplicate files.
