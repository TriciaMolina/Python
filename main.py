from FCFS import FCFS
from Priority_non_preemptive import PriorityNonPreemptive
from PP import PP
from Round_robin import RoundRobin
from SJF_non_preemptive import SJFNonPreemptive
from SRTF import SRTF

# User input for selecting an algorithm
print("Select a scheduling algorithm:")
print("1. FCFS")
print("2. Shortest Job First")
print("3. Non Preemptive Priority")
print("4. Preemptive Priority")
print("5. SRTF")
print("6. Round Robin")

choice = int(input("Enter your choice: "))

if choice == 1:
    fcfs = FCFS()
    no_of_processes = int(input("Enter the number of processes: "))
    fcfs.processData(no_of_processes)
    print('-' * 35 + " FCFS (First Come First Served) " + '-' * 35)
elif choice == 2:
    sjf = SJFNonPreemptive()
    no_of_processes = int(input("Enter the number of processes: "))
    sjf.processData(no_of_processes)
    print('-' * 35 + " SJF (Shortest Job First) " + '-' * 35)
elif choice == 3:
    npp = PriorityNonPreemptive()
    no_of_processes = int(input("Enter the number of processes: "))
    npp.processData(no_of_processes)
    print('-' * 35 + " NPP (Non Preemptive Priority) " + '-' * 35)
elif choice == 4:
    pp = PP()
    no_of_processes = int(input("Enter the number of processes: "))
    pp.processData(no_of_processes)
    print('-' * 35 + " PP (Preemptive Priority) " + '-' * 35)
elif choice == 5:
    srtf = SRTF()
    no_of_processes = int(input("Enter the number of processes: "))
    srtf.processData(no_of_processes)
    print('-' * 35 + " SRTF (Shortest Remaining Time First) " + '-' * 35)
elif choice == 6:
    rr = RoundRobin()
    no_of_processes = int(input("Enter the number of processes: "))
    rr.processData(no_of_processes)
    print('-' * 35 + " RR (Round Robin) " + '-' * 35)
else:
    print("Invalid choice. Please select a valid option.")
