from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmLayang_Layang:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

         # pasang judul
        Label(mainFrame, text='Luas dan Keliling Layang-Layang').grid(row=0, column=0, columnspan=2, pady=10)
        # pasang Label
        Label(mainFrame, text='Diagonal 1:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Diagonal 2:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtDiagonal1 = Entry(mainFrame) 
        self.txtDiagonal1.grid(row=1, column=1, padx=5, pady=5)  
        self.txtDiagonal2 = Entry(mainFrame) 
        self.txtDiagonal2.grid(row=2, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtKeliling = Entry(mainFrame) 
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan keliling layang-layang 
    def onHitung(self, event=None):
        diagonal1 = float(self.txtDiagonal1.get())
        diagonal2 = float(self.txtDiagonal2.get())
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (math.sqrt((0.5 * diagonal1) ** 2 + (0.5 * diagonal2) ** 2))
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(keliling))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLayang_Layang(root, "Program Luas dan Keliling Layang-Layang")
    root.mainloop() 