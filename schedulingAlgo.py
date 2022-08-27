import numpy as np
import matplotlib.pyplot as plt
import sjf,fcfs,priority

print("Non-preemptive Scheduling is a CPU scheduling technique the process takes the resource (CPU time) and holds it till the process gets terminated or is pushed to the waiting state.\n" 
      "No process is interrupted until it is completed, and after that processor switches to another process.\n"
      "Algorithms that are based on non-preemptive Scheduling are First Come First Serve(FCFS), Shortest Job first(SJF), and non-preemptive priority.")

print("Choose the type of non pre-emptive algorithm you want to use")
print("1.FCFS\n2.SJF")
print("---------------------------")

ch=int(input("Enter Your choice:"))
if(ch==1):
    fcfs.fcfs()
elif(ch==2):
    sjf.sjf()
else:
    print("Invalid Choice")



