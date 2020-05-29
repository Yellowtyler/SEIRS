
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
from tkinter import *

from calculation import Calculate
#root=Tk()
#e = Entry(width=20)

#e.pack()


#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()

#root.mainloop()

calculate = Calculate(100, 1, 0, 0, 0.9, 0.2, 0.5, 0, 0, 0.05, 30, 0.1 )
functions = calculate.findAll()
plt.plot(functions[4], functions[0], 'y')
plt.plot(functions[4], functions[1], 'orange')
plt.plot(functions[4], functions[2], 'r')
plt.plot(functions[4], functions[3], 'g')
plt.xlabel("Дни (t)")
plt.ylabel("Численность")
y_patch = mpatches.Patch(color='y', label='S - Восприимчивые')
orange_patch = mpatches.Patch(color='orange', label ='E - Контактные')
r_patch = mpatches.Patch(color='r', label ='I - Инфицированные')
g_patch = mpatches.Patch(color='g', label ='R - Выздоровевшие')
plt.legend(handles=[y_patch, orange_patch, r_patch, g_patch])
plt.show()