import heapq

class Patient:
    def __init__(self,name,surname,ID_num,priority_level):
        self.name = name
        self.surname = surname
        self.ID_num = ID_num
        self.priority = priority_level
        
    def patientInfo(self):
      return f'Patient: {self.name} {self.surname}, ID: {self.ID_num}, Priority Level: {self.priority}'

# Test this function with my own details to see if it prints correctly
# p1 = Patient('ruben', 'da silva', 9907065112085, 5)
# print(p1.patientInfo())

class Scheduler:
    def __init__(self):
        self.queue = []
        
    def addPatient(self):
        pass
    
    def retrieveNextPatient(self):
        pass
    
    def printWaitingList(self):
        pass
    
    def savePatientToFile(self):
        pass
    
    def readConsultFile(self):
        pass