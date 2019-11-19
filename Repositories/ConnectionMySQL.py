import mysql.connector
import os
import yaml

with open ("config.yaml") as file:
        config = yaml.load(file, Loader = yaml.FullLoader)
        for key,value in config.items():
            os.environ[key] = value

MySQLConnection = mysql.connector.connect(host=os.environ['host'], user=os.environ['user'],
                                password=os.environ['password'], port = os.environ['port'], database = os.environ['database'])
MyCursor = MySQLConnection.cursor()
