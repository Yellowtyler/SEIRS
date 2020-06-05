
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
from tkinter import *
from tkinter.messagebox import showerror
from calculation import Calculate

class LabelEntry(Frame):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.pack(fill=X)

        self.lbl = Label(self, text=text, anchor='w')
        self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.entry = Entry(self)
        self.entry.pack(side=LEFT, fill=X, padx=5)



class App(Tk):

 def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
   super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
   self.title("SEIRS")

   self.frame = Frame(self)
   self.frame.grid(row=0, column=0)
   self.entries = []
   fields = self.createFields()
   for field in fields:
           self.entries.append(LabelEntry(self.frame, field))
   button = Button(self, text="Создать график", command = self.showGraph)
   button.grid(row=1, column=0)
   l0 = Label(self, text=" ")
   l0.grid(row=2, column=0)



 def showGraph(self):
    flag = False
    for entry in self.entries:
        if not entry.entry.get():
          showerror(title = "Ошибка", message = "Заполните все поля!")
          return
   
    calcul = Calculate(float(self.entries[6].entry.get()), float(self.entries[7].entry.get()),
                       float(self.entries[8].entry.get()), float(self.entries[9].entry.get()),
                       float(self.entries[0].entry.get()), float(self.entries[1].entry.get()),
                       float(self.entries[2].entry.get()), float(self.entries[4].entry.get()),
                       float(self.entries[3].entry.get()), float(self.entries[5].entry.get()),
                       float(self.entries[10].entry.get()), float(self.entries[11].entry.get()))
    functions = calcul.findAll()
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




 def createFields(self):
    fields = []
    fields.append("β - коэффициент интенсивности контактов индивидов с последующим инфицированием:")
    fields.append("γ - Коэффициент интенсивности выздоровления инфицированных индивидов:")
    fields.append("σ - величина, обратная среднему инкубационному периоду заболевания:")
    fields.append("ρ - коэффицент интенсивности повторного заражения:")
    fields.append("μ - уровень рождаемости:")
    fields.append("ν - уровень смертности:")
    fields.append("S - Количество восприимчивых до пандемии:")
    fields.append("E - Количество контактных до пандемии:")
    fields.append("I - Количество инфицированных до пандемии:")
    fields.append("R - Количество выздоровевших до пандемии:")
    fields.append("t - Длительность пандемии (дни):")
    fields.append("h - величина шага сетки:")
    return fields


if __name__ == "__main__":
    App().mainloop()