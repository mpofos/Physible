import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
import PySimpleGUI as sg

def checkP(s):
    print("run check p")
    k = 2222222222222222222
    if s.find("p") == 1 or s == "p" :
        s = s.replace("p"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.pi
        else:
            k = np.pi
    elif s.find("π") == 1 or s == "π":
        s = s.replace("π"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.pi
        else:
            k = np.pi

    print(k)
    return k

def checkE(s):
    print("run check e")
    k = 2222222222222222222
    if s.find("e") == 1 or s == "e":
        s = s.replace("e"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
        else:
            k = np.exp(1)

    print(k)
    return k

def checkEP(s):
    print("run check ep")
    k = 2222222222222222222
    if (s.find("pe") == 1 or s.find("ep") == 1) :
        print("in here")
        s = s.replace("e"," ")
        s = s.replace("p"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
            k *= np.pi
        else:
            k = np.exp(1)*np.pi
    print(k)
    return k

def check(s):
    flag = checkEP(s)
    if flag != 2222222222222222222:
        return flag
    flag = checkP(s)
    if flag != 2222222222222222222:
        return flag
    flag = checkE(s)
    if flag != 2222222222222222222:
        return flag
    return float(s)

X = []
Y = []

def addPoint(x1,A):
    A.append(float(x1))
    print(A)
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
layout = [  [sg.Text('Enter plots name:   '), sg.InputText()],
            [sg.Text('Enter Axis X name: '), sg.InputText()],
            [sg.Text('Enter Axis Y name: '), sg.InputText()],
            [sg.Button('Add a Point')],
            [sg.Button('Create Plot')],[sg.Button('Close Window')]
           ]
# Create the Window
window = sg.Window('Degressive Oscillation', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break

    if event in (None,'Add a Point'):
        layout = [
        [sg.Text('Enter x cord: '), sg.InputText()],
        [sg.Text('Enter y cord: '), sg.InputText()],
        [sg.Button('Ok', key=addPoint), sg.Button('Cancel')]]

        pop = sg.Window('Add a Point', layout).Finalize()
        pop.BringToFront()
        while True:
            action, times = pop.read()
            if callable(action):
                addPoint(times[0],X)
                addPoint(times[1],Y)
                break
            if action in (None, 'Cancel'):
                break
        pop.close()

    if event in (None,'Create Plot'):
        x = np.array(X)
        y = np.array(Y)
        # y = 2x
        plt.ylabel((values[2]))
        plt.xlabel((values[1]))
        plt.grid(True)
        plt.title((values[0]))
        m, b = np.polyfit(X, Y, 1)
        xnew = np.linspace(0, 10, num=41, endpoint=True)
        plt.plot(X, Y, 'o')
        plt.plot(x, m*x + b,'--')
        plt.legend(['Actual Points', 'Calculated Plot'], loc='best')
        plt.show()


window.Close()