import heapq

class Patient:
    def __init__(self,name,surname,ID_num,priority_level):
        self.name = name
        self.surname = surname
        self.ID_num = ID_num
        self.priority = priority_level
        
    def patientInfo(self):
      return f"{self.name} {self.surname}, ID: {self.ID_num}, Priority Level: {self.priority}"

# Test this function with my own details to see if it prints correctly
# p1 = Patient("ruben", "da silva", 9907065112085, 5)
# print(p1.patientInfo())

class Scheduler:
    def __init__(self):
        self.queue = PriorityQueue()
        
    def addPatient(self,patient):
        self.queue.addPatient(patient)
        
    def retrieveNextPatient(self):
        return self.queue.retrieveNextPatient()
    
    def printWaitingList(self):
        self.queue.printWaitingList()
                            
    def savePatientToFile(self, patient):
        with open("patients.txt","a") as file:
            file.write(f"{patient.patientInfo()}\n")
        print("This patient has been saved to the file")
    
    def readConsultFile(self):
        with open("patients.txt","r") as file:
            for line in file:
                print(line.strip())
                
class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def addPatient(self,patient):
        heapq.heappush(self.queue, (-patient.priority, patient))
        
    def retrieveNextPatient(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        else:
            return None
    
    def printWaitingList(self):
        for priority, patient in sorted(self.queue, reverse=True):
                    print(patient.patientInfo())
                    
def main():
    scheduler = Scheduler()
    
    while True:
        print("\n1. Add a new patient")
        print("2. Retrieve the next patient in line")
        print("3. Print out the current waiting list")
        print("4. Save this patient's record")
        print("5. Print out all patient records")
        print("6. Close the programme")
        
        choice = input("Select one of the options: ")
        print("\n")
        
        if choice == "1":
            name = input("Enter the patient's name: ")
            surname = input("Enter the patient's surname: ")
            ID_num = input("Enter the patient's ID number: ")
            priority = int(input("Enter the priority status from 1-5 with 5 being highest priority: "))
            patient = Patient(name, surname, ID_num, priority)
            scheduler.addPatient(patient)
            print("\nPatient added successfully!\n")
            
        elif choice == '2':
            patient = scheduler.retrieveNextPatient()
            if patient:
                print(f"\nThe next patient is: {patient.patientInfo()}\n")
            else:
                print("\nThere are no patients in the queue.\n")

        elif choice == '3':
            print("Current waiting list:\n")
            scheduler.printWaitingList()
            print("\n")

            
        elif choice == '4':
            patient = scheduler.retrieveNextPatient()
            if patient:
                scheduler.savePatientToFile(patient)
                print("\nThis patient has been saved to the file\n")
            else:
                print("\nThere is nothing to save to the file\n")
                
        elif choice == '5':
            print("\nAll Records are as follows:\n")
            scheduler.readConsultFile()
            print("\n")
            
        elif choice == '6':
            print("\nCheers!\n")
            break
        else:
            print("\nPlease select a valid option!\n")

if __name__ == "__main__":
    main()