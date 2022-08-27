#from nis import cat
import numpy as np
import matplotlib.pyplot as plt
def fcfs():
    print("FIRST COME FIRST SERVE SCHEDULLING")
    n= int(input("Enter number of processes : "))
    d = dict()
    category_names = [] 

    for i in range(n):
        key = "P"+str(i+1)

        a = int(input("Enter arrival time of process"+str(i+1)+": "))
        b = int(input("Enter burst time of process"+str(i+1)+": "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l
    
    d = sorted(d.items(), key=lambda item: item[1][0])
    
    CT = []

    for i in range(len(d)):
        
        if(i==0):
            CT.append(d[i][1][1])
            
            # category_names.append("P"+str(i+1))
    
        
        else:
            CT.append(CT[i-1] + d[i][1][1])
        #category_names.append("P"+str(i+1))
    # category_names.append("P"+str(i))
    
    TAT = []
    for i in range(len(d)):
        TAT.append(CT[i] - d[i][1][0])
    
    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])
    #print(CT)
    #print(category_names) 
    avg_WT = 0
    avg_TAT = 0
    for j in TAT:
        avg_TAT+=j
    avg_TAT=avg_TAT/n
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
    results = {
        'gantchart': CT
        
    }
    print("Process | AT | BT  | CT | TAT| WT |")
    for i in range(n):
        print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",CT[i],"    |    ",TAT[i],"  |   ",WT[i],"   |  ")
        category_names.append(d[i][0])
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


    survey(results, category_names)
    plt.show()