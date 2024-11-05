class Patient:
    def __init__(self,name,surname,ID_num,priority_level):
        self.name = name
        self.surname = surname
        self.ID_num = ID_num
        self.priority = priority_level
        
    def patientInfo(self):
      return f'Patient: {self.name} {self.surname}, ID: {self.ID_num}, Priority Level: {self.priority}'

p1 = Patient('ruben', 'da silva', 9907065112085, 5)
print(p1.patientInfo())