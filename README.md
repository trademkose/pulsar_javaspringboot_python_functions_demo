# Python Pulsar Function script
This repo is created to store my pulsar function demo. 
This function can modify each message on the given input topic and route them to the related topic.

#### Find your Pulsar docker container ID.
docker container ls

#### Enter your Pulsar docker container with the containerID to run process on the container. Starting bash terminal.
docker exec -it containerID bash

#### How to list Pulsar function on Pulsar broker?

./bin/pulsar-admin functions list --tenant public --namespace default


#### How to create a new Pulsar function on Pulsar broker?

./bin/pulsar-admin functions create --py myfirstfunction.py --classname myfirstfunction.MyFirstFunction --tenant public --namespace default --name myfirstfunction --inputs persistent://public/default/topic-new-product

#### How to delete a function on Pulsar broker?

./bin/pulsar-admin functions delete --tenant public --namespace default --name myfirstfunction






