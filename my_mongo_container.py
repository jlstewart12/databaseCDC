import os
import sys

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers


# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('some-mysql')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 1800:1800 --name final_mongo_container -d mongo', 'mongo')
    sys.exit()