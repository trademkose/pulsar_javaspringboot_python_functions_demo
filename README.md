# pulsar_javaspringboot_python_functions_demo
this repo is created to store my pulsar function demo. it can modifies each data and route them to the related topic.



./bin/pulsar-admin functions list --tenant public --namespace default



bin/pulsar-admin functions create --py myfirstfunction.py --classname myfirstfunction.MyFirstFunction --tenant public --namespace default --name myfirstfunction --inputs persistent://public/default/topic-new-product


./bin/pulsar-admin functions delete --tenant public --namespace default --name myfirstfunction






