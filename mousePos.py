#! python3
# mouseNow.py - Display the mouse cursor's current position.

import pyautogui
import tkinter as tk 
import tkinter.ttk as ttk

##print('Press Ctrl-C to quit.')
##try:
##    while True:
##        # Get ang print the mouse coordinates.
##        x, y = pyautogui.position()
##        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
##        pixelColor = pyautogui.screenshot().getpixel((x, y))
##        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
##        positionStr += ', ' + str(pixelColor[1]).rjust(3)
##        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
##        print(positionStr, end='')
##        print('\b' * len(positionStr), end='', flush=True)
##except KeyboardInterrupt:
##    print('\nDone.')

class MousePos():

    def __init__(self, master):
        self.master = master
        master.title('MousePos')
        self.framePos = ttk.LabelFrame(self.master, text='Position')
        self.framePos.pack(fill='both', expand='y', padx=5, pady=5)
        self.frameCol = ttk.LabelFrame(self.master, text='Color')
        self.frameCol.pack(fill='both', expand='y', padx=5, pady=5)
        self.widget()
        self.master.after(10, self.update)

    def widget(self):
        self.xPos = tk.Label(self.framePos, text='X:')
        self.xPos.grid(row=0, column=0)
        self.yPos = tk.Label(self.framePos, text='Y:')
        self.yPos.grid(row=1, column=0)
        self.entXVar = tk.StringVar()
        self.entX = tk.Entry(self.framePos,
                             textvariable=self.entXVar)
        self.entX.grid(row=0, column=1)
        self.entYVar = tk.StringVar()
        self.entY = tk.Entry(self.framePos,
                             textvariable=self.entYVar)
        self.entY.grid(row=1, column=1)

        self.colorRed = tk.Label(self.frameCol, text='Red:')
        self.colorRed.grid(row=0, column=0)
        self.colorGreen = tk.Label(self.frameCol, text='Red:')
        self.colorGreen.grid(row=0, column=2)
        self.colorBlue = tk.Label(self.frameCol, text='Red:')
        self.colorBlue.grid(row=0, column=4)
        self.entRedVar = tk.StringVar()
        self.entRed = tk.Entry(self.frameCol,
                               textvariable=self.entRedVar, width=3)
        self.entRed.grid(row=0, column=1)
        self.entGreenVar = tk.StringVar()
        self.entGreen = tk.Entry(self.frameCol,
                                 textvariable=self.entGreenVar, width=3)
        self.entGreen.grid(row=0, column=3)
        self.entBlueVar = tk.StringVar()
        self.entBlue = tk.Entry(self.frameCol,
                                textvariable=self.entBlueVar, width=3)
        self.entBlue.grid(row=0, column=5)

    def update(self):
        self.xm, self.ym = pyautogui.position()
        self.pixelColor = pyautogui.screenshot().getpixel((self.xm, self.ym))
        self.entXVar.set(self.xm)
        self.entYVar.set(self.ym)
        self.entRed.insert(0, self.pixelColor[0])
        self.entGreen.insert(0, self.pixelColor[1])
        self.entBlue.insert(0, self.pixelColor[2])
        self.master.after(10, self.update)

def main():
    window = tk.Tk()
    app = MousePos(window)
    window.mainloop()

if __name__== '__main__':
    main()
