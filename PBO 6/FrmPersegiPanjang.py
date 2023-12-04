from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang judul
        Label(mainFrame, text='Luas dan Keliling Persegi Panjang').grid(row=0, column=0, columnspan=2, pady=10)

        # pasang Label
        Label(mainFrame, text='Panjang:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=1, column=1, padx=5, pady=5)  
        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=2, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame) 
        self.txtKeliling.grid(row=6, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)
                   
    # fungsi "onHitung" berfungsi untuk menghitung luas dan keliling persegi panjang  
    def onHitung(self, event=None):
        panjang = int(self.txtPanjang.get())
        lebar = int(self.txtLebar.get())
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPersegiPanjang(root, "Program Luas dan Keliling Persegi Panjang")
    root.mainloop()