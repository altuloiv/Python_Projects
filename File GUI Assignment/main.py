
import tkinter
from tkinter import *
from tkinter import filedialog as fd
import shutil
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('HTML Assignment')
        self.master.config(bg='darkgray')

        self.varBody = StringVar()


        self.btnSel = Button(self.master, text="To Copy:", width=10, height=2, command=self.selectFolder1)
        self.btnSel.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay1 = Label(self.master, text="", font=("Helvetica",16), fg='black', bg='darkgray')
        self.lblDisplay1.grid(row=3, column=1, padx=(30,0),pady=(30,0))



        ######## Button 2 #####
        self.btnDes = Button(self.master, text="Destination:", width=10, height=2, command=self.destination)
        self.btnDes.grid(row=2,column=0,padx=(30,0),pady=(30,0))


        #################

        

        self.btnSubmit = Button(self.master, text="Check Files", width=10, height=2, command=self.check)
        self.btnSubmit.grid(row=3, column=1, padx=(0,0),pady=(30,0), sticky=NE)
        
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=3, column=1, padx=(0,90),pady=(30,0), sticky=NE)

    def selectFolder1(self):
        fd.askdirectory()

    def destination(self):
        fd.askdirectory()


    
    

    

    
            
    
    def cancel(self):
        self.master.destroy()
        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
