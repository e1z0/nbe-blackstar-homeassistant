import json
import re
import settings

def strip_invalid(text):
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        return re.sub(r"\s+", '_', text).lower()

class Resource:
    def __init__(self,component,type,resource):
        self.component = component
        self.type = type
        self.resource = resource
    def getHaTopic(self):
        return settings.config["ha_prefix"] + "/"+ self.type + "/" + self.component.device.getUid() + "/"+ self.component.getUid() + "/config"
    def getCommandTopic(self):
        return self.component.command_topic
    def getTempCommandTopic(self):
        return self.component.temperature_command_topic
    def getTempStateTopic(self):
        return self.component.temperature_state_topic
    def getStateTopic(self):
        return self.component.state_topic

class Device:
    def __init__(self,identifiers,name,sw_version,model,manufacturer):
        self.identifiers = identifiers
        self.name = name
        self.sw_version = sw_version
        self.model = model
        self.manufacturer = manufacturer
    def getName(self):
        return self.name
    def getUid(self):
        return strip_invalid(self.name)
    def getId(self):
        return self.identifiers
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=5)

class Climate:
   def __init__(self,name,icon,current_temp_topic,max_temp,device):
        self.temperature_unit = "C"
        self.current_temperature_topic = device.getUid() + "/" + current_temp_topic
        self.temperature_command_topic = device.getUid() + "/climate/" + strip_invalid(name) + "/command"
        self.temperature_state_topic = device.getUid() + "/climate/" + strip_invalid(name) + "/state"
        #self.json_attributes_topic = device.getUid() + "/climate/" + strip_invalid(name)
        self.icon = icon
        self.name = name
        self.max_temp = max_temp
        self.min_temp = 0
        self.modes = [ "auto" ]
        self.mode_state_topic = device.getUid()+"/bridge/static_auto_state"
        self.unique_id = strip_invalid(self.name) + "_" + device.getId()
        self.device = device
        self.availability_topic = device.getUid()+"/bridge/state"
        self.device = device
   def getUid(self):
        return strip_invalid(self.name)
   def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=5)

class Switch:
    def __init__(self,icon,name,device):
        self.icon = icon
        self.name = name
        self.state_topic = device.getUid() + "/switch/" + strip_invalid(name) + "/state"
        self.command_topic = device.getUid() + "/switch/" + strip_invalid(name) + "/command"
        self.availability_topic = device.getUid()+"/bridge/state"
        self.unique_id = strip_invalid(self.name) + "_" + device.getId()
        self.device = device
        self.payload_on = "ON"
        self.payload_off = "OFF"
    def getUid(self):
        return strip_invalid(self.name)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=7)

class Sensor:
    def __init__(self,icon,device_class,unit_of_measurement,state_class,name,device):
        if icon != "none":
           self.icon = icon
        if device_class != "none":
           self.device_class = device_class
        if unit_of_measurement != "none":
           self.unit_of_measurement = unit_of_measurement
        if state_class != "none":
           self.state_class = state_class
        self.name = name
        self.state_topic = device.getUid() + "/sensor/" + strip_invalid(name) + "/state"
        self.availability_topic = device.getUid()+"/bridge/state"
        self.unique_id = strip_invalid(self.name) + "_" + device.getId()
        self.device = device
    def getUid(self):
        return strip_invalid(self.name)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=8)
