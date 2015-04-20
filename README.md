# IFI-protobuf
A client and server implemented in different languages and commucating with <a href="https://developers.google.com/protocol-buffers/">protobuff protocol</a>

##Description
There are 3 folders :
 1. server : the python server
 2. client : the java client
 3. resources : the protocol messages will be used to generate message object in the required languages (java and python) using <a href="http://sergei-ivanov.github.io/maven-protoc-plugin/">maven-protoc-plugin</a>  

##How to
Run server from project root path :
* <b>Required</b> : <a href ="https://github.com/google/protobuf/tree/master/python#installation">Install python module protobuff</a>
* from console : python server/src/main/server.py
* <i>server run on 127.0.0.1:10000</i>

Run client from project root path :
* from console
 * <i>java -jar client/target/client-0.0.1-SNAPSHOT-jar-with-dependencies.jar \<username\> [port [ip [timeout]]</i>
* Default values
 - port : 10000
 - ip : 127.0.0.1
 - timeout : 5000
 
Generate proto messages : <i>mvn clean compile</i>
