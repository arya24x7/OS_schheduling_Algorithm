import numpy as np
import matplotlib.pyplot as plt
def sjf():
    print("SHORTEST JOB FIRST SCHEDULLING")
    n= int(input("Enter number of processes : "))
    d = dict()
 


    for i in range(n):
        key = "P"+str(i+1)

        a = int(input("Enter arrival time of process"+str(i+1)+": "))
        b = int(input("Enter burst time of process"+str(i+1)+": "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l

    dn=d.values()
    #print(dn)
    d = sorted(d.items(), key=lambda item: item[1][1])
    #print(d)
    # print(d)
    k=n
    comp=0
    CT=[0]*n
    done=[0]*n
    process=[]

    # print(d)
    #4print(d[0][0])
    #print(d[1][1][0])
    while(k>0):
        i=0
        while(i<n):
            
            print(d[i][0])
            if d[i][0] in done or d[i][1][0]>comp:
                print(d[i][0]+"skipped")
                i+=1
                #4
                
                
            else:
                # print(d[i][0])
                CT[i]=comp+d[i][1][1]
                comp+=d[i][1][1]
                k=k-1
                done[i]=d[i][0]
                print("added"+d[i][0])
                i=0
    t=0   
    #print(len(CT))        
    while t<len(CT):
        j=t
        print(str(CT[t])+"outer")
        while j<len(CT):
            print(str(CT[j])+"inner"+str(j))
            if CT[t]>CT[j]:
                CT[j],CT[t]=CT[t],CT[j]
                done[j],done[t]=done[t],done[j]
            j+=1
        t+=1        


    print(CT)
    print("hello")
    TAT = [0]*n
    for j in range(len(d)):
        TAT[j]=CT[j] - d[j][1][0]
    
    WT = [0]*n
    for j in range(len(d)):
        WT[j]=TAT[j] - d[j][1][1]
    avg_WT = 0
    avg_TAT = 0
    for j in TAT:
        avg_TAT+=j
    avg_TAT=avg_TAT/n
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
    print(CT)
    results = {
        'gantchart': CT
        
    }
    print("Process | AT | BT  | CT | TAT| WT |")
    for i in range(n):
        print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",CT[i],"    |    ",TAT[i],"  |   ",WT[i],"   |  ")
        #process.append(d[i][0])

    print("Average Waiting Time: ",avg_WT)
    print("Average Turnaround Time: ",avg_TAT)

    #category_names = []



    def survey(results, category_names):
    
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.colormaps['RdYlGn'](
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 2))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            rects = ax.barh(labels, widths, left=starts, height=0.01,
                            label=colname, color=color)

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            ax.bar_label(rects, label_type='center', color=text_color)
        ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                loc='lower left', fontsize='small')

        return fig, ax

    #4
    # results=sorted()
    survey(results, done)
    plt.show()
                

        
    #print(d.items())
    #d = sorted(d.values(), key=lambda item: item[1][0])
    # print(d)2

    #print(d)