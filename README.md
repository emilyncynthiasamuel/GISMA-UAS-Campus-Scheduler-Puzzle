# Campus Scheduler Puzzle
## M603 Advanced Algorithms
### Campus Scheduler System

This Project has the system that uses a mix of both Real and Simulated Dataset of University which comprises of Professors, Modules, Student Groups, Rooms, Campuses, Intakes, Completed Modules, Professor Requirements and Few Restrictions and Public Holidays and the objective is to give the logic timetable and avoiding any Scheduling Conflicts and reducing Unused Room Capacity.

This demonstrates the University Campus's Timetable Scheduler using these four algorithmic approaches as follows:
(i) Greedy Scheduling
(ii) Graph Theory 
(iii) Dynamic Programming for Room Optimization 
and
(iv) Recursive Backtracking

## Project Objectives

The Campus Scheduling System is designed to:
(i) Schedule University Classes into Available Time Slots and Rooms
(ii) Identify any Professor and Student Class Group conflicts for Schedule
(iii) Give priority to Larger Class Sizes during the initial scheduling stage
(iv) Use Graph Coloring to assign any Conflict Free Time Slots
(v) Optimize Room Allocation by minimizing the Unused Room Capacity.
(vi) Recover Any Classes that could not initially be scheduled using Backtracking
(vii) Prevent Duplicate Booking for Rooms, Professors and Student Class Groups.
(viii) Follow the Room Capacity, campus allocation.
(ix) Give Priority to Professor Availability and Restrictions, Completed Student Modules, Different Student Academic Intakes, Public Holidays
(x) Generate the Fnal Schedule Timetable and Validation Reports

# 1. System Requirements
## Software Requirements

(i) Windows 10 or Windows 11
(ii) Python 3.13 or Any Compatible Python 3.X Version
(iii) Visual Studio Code and PowerShell or Command Prompt

Kindly Note: No Database Server is required and no External API is required.

## Hardware Requirements

(i) Operating System: Windows 10 or Windows 11
(ii) Processor: Intel Core i3 or higher
(iii) RAM: 4 GB minimum
(iv) Storage: Approximately 500 MB Free Space

# 2. Development Environment
## IDE
Visual Studio Code is used as the Development Environment.

## Programming Language
Python 3.13

## Data Format
JSON is used for the input dataset and the Main Dataset is:
data/constraints.json

The JSON file contains the following information:
(i) University, Campus and Room Information
(ii) Academic Structure, Module information, Module Repetitions and Teaching schedule
(iii) Professor and Scheduling Constraints
(iv) Public Holidays
(v) Student Groups and Simulated Student Information
(vi) Test Settings

## Data Framework / Database
No database framework is used and this Project uses Python's built-in JSON handling.

# 3. Project Structure

GISMA_UAS_Campus_Scheduler_Puzzle/
|
|--> data/
│   |--> constraints.json
│
|--> output/
│   |--> conflict_report.txt
│   |--> scheduling_report.txt
│   |--> timetable.csv
│
|--> src/
|   |--> __pycache__
│   |--> backtracker.py
│   |--> data_loader.py
│   |--> graph_engine.py
│   |--> greedy_solver.py
│   |--> main.py
│   |--> models.py
│   |--> optimizer.py
│   |--> reporter.py
│   |--> validator.py
│
|--> README.md
|--> requirements.txt

### System Components and Implementation Files

(i) data_loader.py: It reads the JSON Dataset.
(ii) models.py: It defines the Data Structures for Rooms, Modules, Student Groups and Scheduled Classes.
(iii) greedy_solver.py: It builds the Initial Schedule
(iv) graph_engine.py: It constructs Conflict Graphs and applies Welsh-Powell Coloring
(v) optimizer.py: It uses Dynamic Programming to optimize Room Allocation by minimizing the total Unused Seating Capacity.
(vi) backtracker.py: It handles Recursive Function for any Unresolved Classes
(vii) validator.py: It checks the timetable for Hard Constraint Conflicts
(viii) reporter.py: It generates the Output CSV and text reports
(ix) main.py: It carries out the entire Execution Pipeline.

# 4. Dataset

The project uses mix of both Real Data and Simulated Data stored in data/constraints.json

The Dataset contains Two Campuses namely the Berlin Campus and Potsdam Campus.

### Berlin Campus

GISMA Berlin-Donaustraße Campus

Rooms are as follows:
D001 - 30 seats
D002 - 40 seats
D003 - 50 seats
D004 - 60 seats
D005 - 80 seats

### Potsdam Campus

GISMA Potsdam Campus

Rooms are as follows:
Room 1 - 30 seats
Room 2 - 40 seats
Room 3 - 50 seats
Room 4 - 60 seats
Room 5 - 80 seats
Room 6 - 40 seats
Room 7 - 50 seats
Room 8 - 60 seats
Room 9 - 80 seats
Room 10 - 100 seats
Room 11 - 40 seats
Room 12 - 50 seats
MacPool - 35 seats
Auditorium - 150 seats

Also, the dataset contains the following information:
(i) 56 Professors, Four Intakes and Campus Opening Hours
(ii) Foundation, Bachelor, Pre-Masters and Masters Academic Levels
(iii) Student Groups and Simulated Student Data
(iv) Professor Availability Restrictions and List of Public Holidays
(v) Group allocation for Large Class Sizes and Scheduling Constraints

# 5. Algorithms Used

## Stage 1 - Greedy Scheduling
File: src/greedy_solver.py

The Greedy Algorithm creates the Baseline timetable and the Classes are sorted according to the Number of Students, with Larger Class Sizes processed first due to priority. The first Possible Room and Time Slot combination is selected and the Greedy Algorithm Method does not search for the global optimum but it provides a fast solution in the initial.

For each class, the algorithm checks:
(i) Available Days, Available Time Slots
(ii) Suitable Class Room and Room Capacity
(iii) Professor Availability, Professor Duplicate Booking and Student Groups Duplicate Booking

### Complexity (Big O Notation)

O(C×T×R) where:
-> C = Number of Classes
-> T = Number of Available Time Slots
-> R = Number of Rooms

# 6. Graph Theory - Welsh-Powell Graph Coloring

File: src/graph_engine.py

Here, a Conflict Graph is made before assigning the Final Time Slots, where each Class is represented as a Node and an Edge is created between the two Classes when they use the same Professor or if they belong to the same Student Group and the Welsh-Powell Graph Coloring processes the Nodes according to their Number of Conflicts and each color represents a Time Slot, and since two connected Classes cannot receive the same color, classes sharing a Professor or Student Group are successfully assigned to different Time Slots.

### Complexity (Big O Notation)

O(V^2) where:
-> V = Number of Class Nodes

# 7. Dynamic Programming For Room Optimization

File: src/optimizer.py

Here, the Dynamic Programming approach is used to optimize Room Allocation after the Class Time Slots have been allocated and the objective is to minimize the total Unused Seating Capacity while also ensuring that each Class is allocated to a suitable Room within the same Campus and for each Time Slot, the algorithm considers the Classes that needs Rooms and checks all the possible Room Allocation. A Room can only be used once within the same Time Slot and on the other hand, the Rooms that do not have enough capacity for a Class are not considered.

The Waste for assigning a Class to a Room is calculated as:
Waste=Room Capacity-Number of Students

For Example:
Students = 30
Room Capacity = 40
Waste = 10 Seats

The Dynamic Programming approach optimizes the Room Allocation after the Time Slots have been allocated or every scheduled class, the algorithm searches the Available Class Rooms within the same Campus and selects the room with the smallest and least Unused Seating Capacity and the rooms that are already occupied during the same Time Slot are ignored, ensuring that each room is used only once and this reduces the overall Room Capacity Waste while keeping the Timetable unchanged.

The Algorithm stores any previously calculated states and so in that case the same subproblem doesn't need to be solved repeatedly and this saves the memory.

The Recurrence considers each possible Unused Room and calculates:
Total Waste=Current Room Waste+Minimum Waste for the Remaining Classes

And, the Room Allocation with the Minimum Total Waste is selected as to reduce and minimize the Unused Room Capacity and thhis avoids repeatedly solving the same Room Allocation subproblems and provides an optimized Room Allocation for each Time Slot.

### Complexity (Big O Notation)

O(C×2^RxR) where:
-> C = Number of Scheduled Classes
-> R = Number of Available Class Rooms

# 8. Best-Effort Backtracking

File: src/backtracker.py

Here, Backtracking is used as the Recovery Mechanism for Classes that could not be placed in the Initial Period and the algorithm recursively attempts different Day, Time Slot, and Room combinations (Day + Time Slot + Room) and also, includes checking the Room Capacity, Room Availability, Professor Availability (including their Restrictions) and Double (Duplicate) Booking Constraints. Any invalid or not possible allocations are rejected before the Recursive Attempts continue and the best partial solution is retained to recover as many Unresolved Classes as possible and in case if a class cannot be recovered, then it remains Unscheduled and is always reported for a manual intervention only.

### Complexity (Big O Notation)

O((TxR)^C) worst case where:
-> T = Number of Available Time Slots
-> R = Number of Rooms
-> C = Number of Unresolved Classes

Kindly Note: Backtracking is only applied to the remaining Unresolved Classes rather than applying to the Entire Timetable.

# 9. Algorithm Justification

(i) Stage: 1
Algorithm: Greedy Scheduling
Complexity: O (CxTxR)
Justification: It gives quickly a Basline by assigning each Class to the first Possible Class Room and Time

(ii) Stage: 2
Algorithm: Welsh-Powell Graph Coloring
Complexity: O(V^2)
Justification: It models the Professor and the Student Group Conflicts aslways before the Final Time Slot Allocation.

(iii) Stage: 3
Algorithm: Dynamic Programming
Complexity: O(Cx2^R×R)
Justification: It finds the Class Room Allocations with the Minimum Total Unused Capacity

(iv) Stage: 4
Algorithm: Recursive Backtracking
Complexity: O((T×R)^C)
Justification: It recovers the Unresolved Classes while removing any impossible allocations.

And, here:
C = Number of Classes
T = Number of Available Time Slots
R = Number of Rooms
V = Number of Graph Nodes or the Classes

# 10. Campus Scheduling Project Workflow

The GISMA UAS Campus Scheduler System follows this Project Workflow:

constraints.json
       |
       v
Data Loading
       |
       v
Creating Class Request 
       |
       v
Stage 1: Greedy Baseline
       |
       v
Stage 2: Conflict Graph
       |
       v
Welsh-Powell Coloring
       |
       v
Stage 3: Dynamic Programming Fpr Room Optimization
       |
       v
Stage 4 Best-Effort Backtracking
       |
       v
Then, Final Validation
       |
       v
Reports

The Main Execution File is: src/main.py

# 11. How to Run the Project

## Step 1 - Download or Clone the Repository
(i) You can Download the Project from GitHub or even Clone it using Git.

For Example:
git clone https://github.com/emilyncynthiasamuel/GISMA-UAS-Campus-Scheduler-Puzzle

(ii) Then enter the project folder:
cd GISMA_UAS_Campus_Scheduler_Puzzle

## Step 2 - Check Python
Open PowerShell in your Project Folder and then run this:

python --version
and this will return the expected -> Python 3.13.x

And, if Python is installed correctly, continue to the next below steps.

## Step 3 - Create a Virtual Environment
You need to run this: 
python -m venv .venv

## Step 4 - Activate the Virtual Environment
On Windows PowerShell:
.venv\Scripts\Activate.ps1

The terminal should show something similar to:
(.venv) PS C:\...\GISMA_UAS_Campus_Scheduler_Puzzle>

## Step 5 - Install Requirements
Run this:
pip install -r requirements.txt

Kindly Note: This project uses standard Python Functionality and does not require any External Scheduling Libraries.

## Step 6 - Open the Project in Visual Studio Code
From the Project Folder:
code .

Alternatively you can open Visual Studio Code manually and select:
GISMA_UAS_Campus_Scheduler_Puzzle

## Step 7 - Check the Dataset
Open:
data/constraints.json

The Scheduler reads this file automaticall and kindly, make sure to not move the file from the data folder.

## Step 8 - Run the Scheduler
From the Root Project Folder, run:
python src/main.py

The exact Room Waste may change if the Dataset or Algorithm Implementation is changed but the Expected Output is similar to the following:
Campus Puzzle Scheduler
_______________________
Scheduled classes: 79
Unscheduled Classes: 0
Room capacity waste: 1396
Validation conflicts: 0

Reports created in Output Folder.

# 12. Output Files
After the Execution, the following files are created in this folder called: output/

### timetable.csv
The file timetable.csv comprises of the generated Timetable including the following information: 
Class ID, Module, Module Name, Student Group, Section, Professor, Day, Time, Room, Campus and Student Count

### scheduling_report.txt
The file scheduling_report.txt comprises the Scheduling Summary of the following information: Total Scheduled Classes, Room Capacity Waste and Validation Results which are generated after the executiion.

### conflict_report.txt
The file conflict_report.txt comprises of the informatio which is about the Detected Scheduling Conflicts and if there are no conflicts are detected, the Report states that No Hard Constraint Conflicts were found.

# 13. Current Test Result
Using the current constraints.json Dataset, the Scheduler gave the following output:
Scheduled Classes: 79
Unscheduled Classes: 0
Room Capacity Waste: 1396 Seats
Validation Conflicts: 0

And, this output means the current Execution successfully produced a Timetable for all the generated class requests without any validation conflicts and the 1396 Seats represent the Unused Room Capacity across the allocated Rooms and this is an Optimization Metric and this does not mean that 1396 Students were affected.

# 14. Validation

The Final Timetable is checked for the following details:
Room Capacity, The Correct Campus Room, Room's Duplicate booking, Professor Conflicts, Student Group Conflicts and Missing Room Allocation.

And, the current execution reports:
Validation conflicts: 0

# 15. Manual Fix Log

In the current Execution, the output includes all 79 Generated Class Requests which were successfully Scheduled. Therefore, no manual intervention was required but if a Dataset in the future gives an Unscheduled Classes because of Insufficient Rooms, Unavailable Professors or sometimes Limited Time Slots, then, the Conflict Report identifies those classes so that a University Scheduler can manually allocate additional rooms or modify the timetable.

# 16. GitHub Repository

GitHub Repository Link:
https://github.com/emilyncynthiasamuel/GISMA-UAS-Campus-Scheduler-Puzzle

# 17. Video Demonstration

Video Demonstration Link:
https://www.youtube.com/watch?v=2jiAOmeUjlc

The Video Demonstration shows the following details:
Project Structure, Dataset, Main Execution, Greedy Scheduling Algorithm, Conflict graph and Welsh-Powell Coloring, Dynamic Programming Room Optimization, Backtracking, Final Timetable, Validation Result and the Generated Reports.

# 18. Conclusion

This Campus Scheduler Project shows that how different Algorithms Techniques can be used to solve the University Timetable Scheduling Problem. Here, the Greedy Algorithm gives a quick baseline solution, while the Graph Theory gives the relationships between the Classes and uses the Welsh-Powell Coloring to avoid any conflicts between the Professor and the Student-Group.
While Dynamic Programming optimizes the Room Allocation by minimizing any Unused Seating Capacity, on the other hand, Backtracking gives the Recovery Mechanism for any Unresolved Classes.

The Final Validation Stage checks the generated timetable and it provides the Reports for further evaluation and sometimes a Manual Intervention might be required. In conclusion, this Project demonstrates the Practical Applications of Greedy Algorithm, Graph Theory, Dynamic Programming and Backtracking to the real-world University Timetable Scheduling Problem.



