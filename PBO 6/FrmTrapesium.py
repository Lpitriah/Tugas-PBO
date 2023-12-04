from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmTrapesium:
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
        Label(mainFrame, text='Luas dan Keliling Trapesium').grid(row=0, column=0, columnspan=2, pady=10)

        # pasang Label
        Label(mainFrame, text='Sisi a:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi b:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtSisi_a = Entry(mainFrame) 
        self.txtSisi_a.grid(row=1, column=1, padx=5, pady=5)  
        self.txtSisi_b = Entry(mainFrame) 
        self.txtSisi_b.grid(row=2, column=1, padx=5, pady=5) 
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=3, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5) 
        self.txtKeliling = Entry(mainFrame) 
        self.txtKeliling.grid(row=6, column=1, padx=5, pady=5) 
        
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan keliling trapesium 
    def onHitung(self, event=None):
        sisi_a = float(self.txtSisi_a.get())
        sisi_b = float(self.txtSisi_b.get())
        tinggi = float(self.txtTinggi.get())                  
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        keliling = sisi_a + sisi_b + 2 * (math.sqrt((tinggi ** 2) + (((sisi_b - sisi_a) ** 2) / 4)))
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(keliling))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTrapesium(root, "Program Luas dan Keliling Trapesium")
    root.mainloop() 