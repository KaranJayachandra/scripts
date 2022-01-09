from configparser import ConfigParser

CONFIGURATIONFILE = "configurations.ini" 

def setConfig(property, value):
    configFile = ConfigParser()
    configFile.read(CONFIGURATIONFILE)
    stringValue = '['
    if isinstance(value, list):
        for item in value:
            stringValue += str(item) + ','
        stringValue = stringValue[:-1] + ']'        
    else:
        stringValue = str(value)
    configFile['DEFAULT'][property] = stringValue
    with open(CONFIGURATIONFILE, 'w') as configFilePointer:
        configFile.write(configFilePointer)
        configFilePointer.flush()
        configFilePointer.close()

def getConfig(property):
    configFile = ConfigParser()
    configFile.read(CONFIGURATIONFILE)
    stringValue = configFile['DEFAULT'][property]
    if ('[' in stringValue and ']' in stringValue):
        stringValue = stringValue.replace('[', '')
        stringValue = stringValue.replace(']', '')
        output = stringValue.split(',')
    else:
        output = stringValue
    return output
