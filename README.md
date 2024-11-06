# ER Visit Scheduler

This Python application provides a basic patient management system that prioritizes patients in a queue based on their urgency level. It includes functionality for adding, retrieving, and saving patient records with priority levels, along with reading saved records from a file.

## Project Structure

- `scheduler.py`: The main Python script containing all classes and logic for managing patients in a priority queue.
- `patients.txt`: A text file where patient records are saved for future reference.

## Classes

### Patient
The `Patient` class represents a patient with attributes:
- `name`: The patient's first name.
- `surname`: The patient's last name.
- `ID_num`: The patient's ID number.
- `priority`: An integer priority level, with `5` being the highest priority.

#### Method:
- `patientInfo()`: Returns the patient's information as a formatted string.

### Scheduler
The `Scheduler` class manages the queue and file operations, including:
- Adding patients to the priority queue.
- Retrieving the next patient based on priority.
- Printing the waiting list of patients.
- Saving and reading patient records from `patients.txt`.

### PriorityQueue
The `PriorityQueue` class handles the internal priority-based ordering of patients using a max-heap.

## How It Works

1. **Add a new patient**: Adds a patient to the queue with priority.
2. **Retrieve the next patient**: Retrieves and removes the patient with the highest priority from the queue.
3. **Print out the current waiting list**: Displays all patients currently in the queue.
4. **Save this patient's record**: Saves the patient’s details from the queue to `patients.txt`.
5. **Print out all patient records**: Reads and displays all saved records from `patients.txt`.
6. **Close the program**: Exits the application.

## Getting Started

### Prerequisites
- Python 3.6+

### Running the Application
1. Clone or download the project folder.
2. Open a terminal in the project directory.
3. Run the following command to start the application:
   ```bash
   python scheduler.py