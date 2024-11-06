import heapq

class Patient:
    def __init__(self,name,surname,ID_num,priority_level):
        self.name = name
        self.surname = surname
        self.ID_num = ID_num
        self.priority = priority_level
        
    def patientInfo(self):
      return f"Patient: {self.name} {self.surname}, ID: {self.ID_num}, Priority Level: {self.priority}"

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
                            
    def savePatientToFile(self, patient, status):
        with open("patients.txt","a") as file:
            file.write(f"Patient: {patient} >> Status: {status}\n")
    
    def readConsultFile(self):
        with open("patients.txt","r") as file:
            for line in file:
                print()
                
class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def addPatient(self,patient):
        heapq.heappush(self.patients_queue, (-patient.priority, patient))
        
    def retrieveNextPatient(self):
        if self.patients_queue:
            return heapq.heappop(self.patients_queue)[1]
        else:
            return None
    
    def printWaitingList(self):
        for priority, patient in sorted(self.patients_queue, reverse=True):
                    print(patient)
                    
def main():
    scheduler = Scheduler()
    
    while True:
        print("1. Add a new patient")
        print("2. Retrieve the next patient in line")
        print("3. Print out the current waiting list")
        print("4. Save this patient's record")
        print("5. Print out all patient records")
        print("6. Close the programme")
        
        choice = input("Select one of the following options: ")
        
        if choice == "1":
            name = input("Enter the patient's name: ")
            surname = input("Enter the patient's surname: ")
            ID_num = input("Enter the patient's ID number: ")
            priority = int(input("Enter the priority status from 1-5 with 5 being highest priority: "))
            patient = Patient(name, surname, ID_num, priority)
            scheduler.add_patient(patient)
        elif choice == '2':
            patient = scheduler.retrieveNextPatient()
            if patient:
                print(f"The next patient is: {patient}")
            else:
                print("There are no patients in the queue.")
        elif choice == '3':
            scheduler.printWaitingList()
        elif choice == '4':
            patient = scheduler.retrieveNextPatient()
            if patient:
                status = input(f"Enter the status for {patient}: ")
                scheduler.savePatientToFile(patient, status)
        elif choice == '5':
            scheduler.readConsultFile()
        elif choice == '6':
            break

if __name__ == "__main__":
    main()