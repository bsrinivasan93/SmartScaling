from cassandra.cluster import Cluster
import logging
import yaml
from fileinput import close
from configManager import ConfigManager
from connection import SimpleClient

log = logging.getLogger()
log.setLevel('INFO')

config_file = 'appconfig.yaml'

class ConnectionManager:
    def __init__(self):
        self.configMgr = None
        self.clientConnections = []
        self.initialize()
        
    def initialize(self):
        self.configMgr = ConfigManager()
        for i in range(0, self.configMgr.getNumConnections() - 1):
            self.clientConnections.append(SimpleClient())
	    
        self.clientConnections[0].connect(self.configMgr.getNodes())
#	self.clientConnections[0].create_schema()
	self.clientConnections[0].load_data()
	self.clientConnections[0].query_schema()
	
   

def main():
    logging.basicConfig()
    manager = ConnectionManager()

if __name__ == "__main__":
    main()
