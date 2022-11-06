import os
import json

def init():
    global config
    curr_path = os.path.dirname(os.path.realpath(__file__))
    config_file = curr_path+"/config.json"
    print ("Checking if settings file exists: ",config_file)
    if (os.path.exists(config_file)):
      with open(config_file) as f:
        config = json.load(f)
        print ("File found, settings loaded!")
    else:
      print ("Settings file "+config_file+" does not exist!")
