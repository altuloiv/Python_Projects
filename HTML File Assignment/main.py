
import tkinter
from tkinter import *
import webbrowser
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


        self.lblBody = Label(self.master, text="Enter Text Here: ", font=("Helvetica",16),fg='black', bg='darkgray')
        self.lblBody.grid(row=0,column=0,padx=(30,0),pady=(30,0))


        self.lblDisplay = Label(self.master, text="", font=("Helvetica",16), fg='black', bg='darkgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0),pady=(30,0))

        self.txtBody = Entry(self.master,text=self.varBody, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBody.grid(row=0, column=1, padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.bodyText)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0),pady=(30,0), sticky=NE)
        
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90),pady=(30,0), sticky=NE)
    def bodyText(self):
        bod = self.varBody.get()
        f = open('helloworld.html', 'w')

        f.write('<html>')
        f.write('<head>')
        f.write('<title>HTML Assignment</title>')
        f.write('</head>')
        f.write('<body')
        f.write("<h2>The text you entered is:</br> {}</h2>".format(bod))
        f.write('</body')
        f.write('</html>')

        f.close()

        filename = 'file:///'+os.getcwd()+'/'+'helloworld.html'
        webbrowser.open_new_tab(filename)
            
    
    def cancel(self):
        self.master.destroy()
        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
