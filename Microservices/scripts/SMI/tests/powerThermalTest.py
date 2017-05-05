'''
Created on May 2, 2017

@author: Rahman Muhammad
'''
import json
import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from handlers.PowerThermalMicroservice import PowerThermalHandler
from utility.UtilBase import Utility



class PowerThermalMicroserviceTest(unittest.TestCase):    
    global logger
    logger = Utility().getLoggerInstance()
    
    def test_getVersion(self):        
                
        try:
           logger.info("PowerThermalMicroserviceTest - test_getVersion() - Running")
           response = PowerThermalHandler().getAPIVersion()
           logger.info("PowerThermalHandlerTest: getAPI: Response: " + response.text)
                      
             
        except Exception as e:
            logger.error("SCPMicroserviceTest:test_exportSCP: Exception: " + str(e))
            raise e
        
    def test_getPowerThermal(self):
           
        
        try:
            logger.info("PowerThermalMicroserviceTest - test_getPowerThermal() - Running")
            response = PowerThermalHandler().getPowerThermal()
            logger.info("PowerThermalHandlerTest: " + response.text)
           
             
        except Exception as e:
            logger.error("PowerThermalMicroserviceTest Exception: " + str(e))
            raise e
        
           
        
if __name__=="__main__":
      unittest.main()
      
    