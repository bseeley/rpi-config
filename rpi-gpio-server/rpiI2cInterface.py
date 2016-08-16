#!/usr/bin/env jython

import com.pi4j.io.i2c.I2CBus as I2CBus
import com.pi4j.io.i2c.I2CDevice as I2CDevice
import com.pi4j.io.i2c.I2CFactory as I2CFactory

class Interface():
    interfaceDevices = []
    def __init__(self):
        self.bus = I2CFactory.getInstance(I2CBus.BUS_1)
    
    def parse(self,num, instr, pinType, pinState, duration):
        targetDevice = None
        for device in Interface.interfaceDevices:
            if device[0] == instr[1:]:
                targetDevice = device[1]             
                break
            else:
                pass
        if not targetDevice:
            return 5
        message = self.createMessage(num, pinType, pinState, duration)
        self.write(targetDevice, message)
        if pinState == "GET":
            self.read(targetDevice)            
        return 0
                
    def createMessage(self, num, pinType, pinState, duration):
        message = str(num)+","+str(pinType)+","+str(pinState)+","+str(duration)
        return message
    
    def createDevice(self, name, busAddress):
        device = self.bus.getDevice(busAddress)
        deviceName = name 
        Interface.interfaceDevices.append([deviceName, device])
        
    def write(self, device, message):
        device.write(message)
            
    def read(self, device):
        device.read(a, 0, 512)
        print a
        
        """
        Reads the entire buffer from target device
        """
        
           