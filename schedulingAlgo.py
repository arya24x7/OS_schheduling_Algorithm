import numpy as np
import matplotlib.pyplot as plt
import sjf,fcfs,priority

print("")

print("Choose the type of non pre-emptive algorithm you want to use")
print("1.FCFS\n2.SJF\n3.PRIORITY")
print("---------------------------")

ch=int(input("Enter Your choice:"))
if(ch==1):
    fcfs.fcfs()
elif(ch==2):
    sjf.sjf()
elif(ch==3):
    priority.priority()
else:
    print("Invalid Choice")



