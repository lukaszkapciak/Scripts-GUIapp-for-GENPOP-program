from tkinter import *

class application(Frame):
    def __init__(self,master):
        super(application,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.input_name=[]
        self.output_name=[]
    def create_widgets(self):
        self.lbl=Label(self,text="FIS-scores from .DIV file (GENPOP output file)")
        self.lbl.grid(row=1,column=0,columnspan=2)
        self.lbl.grid()
        self.lbl=Label(self,text="----------------------------------------------------------------")
        self.lbl.grid(row=2,column=0,columnspan=2)
        self.lbl.grid()
        self.lbl=Label(self,text="Type the full input filename (with format)")
        self.lbl.grid(row=3,column=1,columnspan=2)
        self.lbl.grid()
        self.okno1=Text(self,width=10,height=1)
        self.okno1.grid(row=4,column=1,columnspan=4,ipadx=85)
        self.lbl=Label(self,text="Enter the name of the output file (without format)")
        self.lbl.grid(row=5,column=1,columnspan=2)
        self.lbl.grid()
        self.okno2=Text(self,width=10,height=1)
        self.okno2.grid(row=6,column=1,columnspan=4,ipadx=85)
        self.lbl=Label(self,text="----------------------------------------------------------------")
        self.lbl.grid(row=8,column=1,columnspan=2)
        self.lbl.grid()
        self.okno3=Text(self,width=10,height=5)
        self.okno3.grid(row=9,column=0,columnspan=4,ipadx=85)
        self.btn=Button(self,text="Click!",command=self.przycisk1)
        self.btn.grid(row=7,column=1,ipadx=12,padx=1)
        self.btn.grid()
    def przycisk1(self):
        self.input_name.append(self.okno1.get(0.0,END).strip())
        self.output_name.append(self.okno2.get(0.0,END).strip())
        plik=open(self.input_name[0], "r+")
        plik4=open(self.output_name[0]+'.txt', "w")
        p1=[]
        Fis1=[]
        for i in plik:
            p1.append(i.strip())
        for i in range(len(p1)):
            if p1[i]=='1-Qintra   1-Qinter      Fis':
                lane=p1[i+2]
                lane=lane[-7:]
                Fis1.append(lane)
        for i in Fis1:
            plik4.write(i+'\n')

        plik.close()
        plik4.close()
        self.okno3.delete(0.0,END)
        self.okno3.insert(20.1,'Your Fis-scores files are ready. Check it under "'+self.output_name[0]+'.txt" name in the same folder.')
        self.output_name=[]
        
root=Tk()
root.title("App for Fis scores")
root.geometry("325x280")
app = application(root)
root.mainloop()
