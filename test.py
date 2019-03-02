import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = range(9, 20)
y_pos = np.arange(len(objects))
performance = [1,2,4,8,6,4,3,6,9,6,5]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Waiting time (minutes)')
plt.xlabel('Hours of the day')
plt.title('Monday')
 
plt.show()