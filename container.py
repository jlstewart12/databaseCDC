import os
import sys
import pymysql
from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql, mongodb does not need it



# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')


# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')



# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 5600:5600 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=mypassword -d mysql', 'mysql')
    create('docker run -p 1800:1800 --name final_mongo_container -d mongo', 'mongo')
    create('docker run -p 2400:2400 --name final_redis_container -d redis', 'redis')
    create('docker run -p 1000:1000 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()
