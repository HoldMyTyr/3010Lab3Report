"""
Graphing our data

@author Vee Sutton
@author u1406065
@version Nov, 9, 2024
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#### CHANGE THIS IF WE HAVE DIFFERENT DATA SET TYPE
def convertData(run):
    d1 = np.array(run['1'])
    d2 = np.array(run['2'])
    return d1, d2

#### CHANGE THIS IF WE HAVE DIFFERENT DATA SET TYPE
# change the skiprows, encoding, and delimiter to the cvs file
sample1 = pd.read_csv(r'data\1.csv', skiprows=1, encoding='utf-8', delimiter=',')

#### CHANGE THIS IF WE HAVE DIFFERENT DATA SET TYPE
dataPoint1, dataPoint2 = convertData(sample1)

#######################    PLOT 1    #######################
plt.figure(figsize=(10, 6))
plt.plot(dataPoint1, dataPoint2, 'r-') #data 1
plt.plot(dataPoint1, dataPoint2, 'g-') #data 2
plt.plot(dataPoint1, dataPoint2, 'b-') #data 3
plt.title('title', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.xlabel('xlabel (units)', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.ylabel('ylabe (units)', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.legend(['data 1', 'data 2', 'data 3'], bbox_to_anchor=(1, 1),fontsize=14)
#plt.yticks(np.arange(0,101,10))
plt.grid(True)
#plt.tight_layout()
plt.show()

#plt.savefig('filename.png', dpi=300)
