from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmSegitiga:
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
        Label(mainFrame, text='Luas dan Keliling Segitiga').grid(row=0, column=0, columnspan=2, pady=10)
        
        # pasang Label
        Label(mainFrame, text='Alas:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtAlas = Entry(mainFrame) 
        self.txtAlas.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)    
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtKeliling = Entry(mainFrame) 
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan keliling segitiga
    def onHitung(self, event=None):
        alas = float(self.txtAlas.get())
        tinggi = float(self.txtTinggi.get())
        luas = 0.5 * alas * tinggi
        keliling = alas + 2 * (math.sqrt(alas ** 2 + tinggi ** 2))
        self.txtLuas.delete(0, "end")
        self.txtLuas.insert("end", str(luas))
        self.txtKeliling.delete(0, "end")
        self.txtKeliling.insert("end", str(keliling))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSegitiga(root, "Program Luas dan Keliling Segitiga")
    root.mainloop()