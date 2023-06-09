import tkinter as tk
from tkinter import ttk
import random

from RSA_ENC import *

class ISBN:
    def __init__(self,master):
        master.modeFieldCanvas.destroy()

        master.modeFieldCanvas = tk.Canvas(master.canvas,relief='solid',borderwidth=0.5,bg='light green')
        master.modeFieldCanvas.place(relwidth=1,relheight=0.9,rely=0.096)
        master.modeFieldCanvas.bind("<Button-1>", master.unfocus)
        master.modeFieldCanvas.bind("<Button-3>", master.unfocus)

        self.input = tk.Text(master.modeFieldCanvas,bg='white',borderwidth=0.5,relief='solid',font=('Consolas',14),wrap='word')
        self.input.place(relx=0.01,rely=0.01, relwidth=0.49,relheight=0.6)

        self.textOutput = tk.StringVar()
        self.textOutput.set("MOHON MASUKKAN ANGKA!")

        self.output = tk.Text(master.modeFieldCanvas, bg='white',fg='black', borderwidth=0.5, relief='solid', font=('Consolas', 14),state='disabled',wrap='word')#textvariable=self.textOutput)
        self.output.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.6)

        self.inputButt = tk.Button(master.modeFieldCanvas, bg='white',fg='black',text='CEK',font=master.font,relief='solid',borderwidth=0.5,command= self.processInput)
        self.inputButt.place(relx=0.01,rely=0.62,relwidth=0.2)

    def processInput(self):
        try:
            self.textInput = int(self.input.get("1.0","end-1c"))

            self.textInput = str(self.textInput)
            k = len(self.textInput)
            key = 3
            keykey = []
            kunci = 0

            for i in range(k):
                if key == 1:
                    key = 3;
                else:
                    key = 1
                keykey.append(int(self.textInput[i])*key)

            print(sum(keykey))

            kunci = 10 - (sum(keykey[:k-1]) % 10)
            if sum(keykey) % 10 == 0:
                self.output.configure(state='normal')
                self.output.delete(1.0,tk.END)
                self.output.insert("1.0", "VALID\n")
                self.output.insert("2.0", f"KARAKTER UJI = {kunci}")
                self.output.configure(state='disabled')
            else:
                self.output.configure(state='normal')
                self.output.delete(1.0, tk.END)
                self.output.insert("1.0", f"TIDAK VALID\nHasil = {sum(keykey)} tidak habis dibagi oleh 10")
                self.output.configure(state='disabled')
        except ValueError:
            self.output.configure(state='normal')
            self.output.delete(1.0, tk.END)
            self.output.insert("1.0","MOHON INPUT ANGKA!\n")
            self.output.configure(state='disabled')

class Caesar:
    def __init__(self,master):
        self.master = master
        master.modeFieldCanvas.destroy()
        self.reference1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.reference2 = 'abcdefghijklmnopqrstuvwxyz'
        self.reference3 = '0123456789'

        master.modeFieldCanvas = tk.Canvas(master.canvas, relief='solid', borderwidth=0.5, bg='light yellow')
        master.modeFieldCanvas.place(relwidth=1, relheight=0.9, rely=0.096)
        master.modeFieldCanvas.bind("<Button-1>", master.unfocus)
        master.modeFieldCanvas.bind("<Button-3>", master.unfocus)

        self.input = tk.Text(master.modeFieldCanvas, wrap='word',bg='white', borderwidth=0.5, relief='solid', font=('Arial', 12))
        self.input.place(relx=0.01, rely=0.01, relwidth=0.49, relheight=0.6)

        self.output = tk.Text(master.modeFieldCanvas, bg='white', fg='black', borderwidth=0.5, relief='solid',
                              font=('Arial', 12), state='disabled',wrap='word')  # textvariable=self.textOutput)
        self.output.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.6)

        self.labelMode = tk.Label(master.modeFieldCanvas, bg='white', fg='black',anchor = 'w', text='MODE : ', padx=10,font=master.font,borderwidth=0.5,relief='solid')
        self.labelMode.place(relx=0.01, rely=0.62, relwidth=0.98,relheight=0.09)

        self.encButt = tk.Button(master.modeFieldCanvas, bg='yellow', text='ENKRIPSI',borderwidth=0.5,relief='solid',command=self.enkripsi,state='disabled')
        self.encButt.place(relx=0.11,rely=0.63,relwidth=0.1,relheight=0.07)

        self.decButt = tk.Button(master.modeFieldCanvas, bg='white', text='DEKRIPSI', borderwidth=0.5, relief='solid',command=self.dekripsi)
        self.decButt.place(relx=0.22, rely=0.63, relwidth=0.1, relheight=0.07)

        self.salinButt = tk.Button(master.modeFieldCanvas, bg='white', text='SALIN', borderwidth=0.5, relief='solid',
                                 command=self.salinText)
        self.salinButt.place(relx=0.69, rely=0.63, relwidth=0.1, relheight=0.07)
        self.salinButt.bind("<Enter>",master.entered)
        self.salinButt.bind("<Leave>",master.leaves)

        self.simKeyLabel = tk.Label(master.modeFieldCanvas, bg='white', fg='black', anchor='w', text='KUNCI : ', padx=10,
                                  font=master.font, borderwidth=0.5, relief='solid')
        self.simKeyLabel.place(relx=0.01, rely=0.72, relwidth=0.98, relheight=0.09)

        self.simKey = tk.Text(master.modeFieldCanvas, bg='white', borderwidth=0.5, relief='solid', font=('Consolas', 12),padx=10,pady=10,wrap='none')
        self.simKey.place(relx=0.12, rely=0.73, relwidth=0.3, relheight=0.07)

        self.simKeyButt = tk.Button(master.modeFieldCanvas, bg='white', text='PROSES!', borderwidth=0.5, relief='solid',command=self.proses)
        self.simKeyButt.place(relx=0.43, rely=0.73, relwidth=0.1, relheight=0.07)
        self.encryptedText = ''
        self.simKeyButt.bind("<Enter>", master.entered)
        self.simKeyButt.bind("<Leave>", master.leaves)

    def salinText(self):
        self.master.root.clipboard_clear()
        self.master.root.clipboard_append(''.join(str(i) for i in self.encryptedText))
        self.master.root.clipboard_append('', type='STRING')

    def proses(self):
        self.output.configure(state='normal')
        self.output.delete(1.0, tk.END)
        self.output.insert("1.0", "SEDANG MEMPROSES..." + "\n")
        self.output.configure(state='disabled')
        try:
            self.encryptedText = ''
            self.decryptedText = ''
            self.key = int(self.simKey.get("1.0","end-1c"))
            self.text = self.input.get("1.0","end-1c")

            if self.encButt.cget("state") == "disabled":

                for i in range(len(self.text)):
                    if self.text[i] in self.reference1:
                        self.encryptedText+= self.reference1[(self.reference1.index(self.text[i]) + self.key) % 26]
                    elif self.text[i] in self.reference2:
                        self.encryptedText+= self.reference2[(self.reference2.index(self.text[i]) + self.key) % 26]
                    elif self.text[i] in self.reference3:
                        self.encryptedText += self.reference3[(self.reference3.index(self.text[i]) + self.key) % 10]
                    else:
                        self.encryptedText+=self.text[i]

                self.output.configure(state='normal')
                self.output.delete(1.0,tk.END)
                self.output.insert("1.0", self.encryptedText+"\n")
                self.output.configure(state='disabled')

            else:
                for i in range(len(self.text)):
                    if self.text[i] in self.reference1:
                        self.decryptedText+= self.reference1[(self.reference1.index(self.text[i]) - self.key) % 26]
                    elif self.text[i] in self.reference2:
                        self.decryptedText+= self.reference2[(self.reference2.index(self.text[i]) - self.key) % 26]
                    elif self.text[i] in self.reference3:
                        self.decryptedText += self.reference3[(self.reference3.index(self.text[i]) - self.key) % 10]
                    else:
                        self.decryptedText+=self.text[i]

                self.output.configure(state='normal')
                self.output.delete(1.0,tk.END)
                self.output.insert("1.0", self.decryptedText+"\n")
                self.output.configure(state='disabled')

        except ValueError:
            self.simKey.delete(1.0,tk.END)
            self.output.configure(state='normal')
            self.output.delete(1.0, tk.END)
            self.output.insert("1.0", "MOHON MASUKKAN KUNCI BERUPA BILANGAN BULAT" + "\n")
            self.output.configure(state='disabled')
    def enkripsi(self):
        self.encButt.configure(state='disabled',bg='yellow')
        self.decButt.configure(state='normal',bg='white')
        self.salinButt.configure(state='normal',bg='white')
    def dekripsi(self):
        self.decButt.configure(state='disabled',bg='yellow')
        self.encButt.configure(state='normal',bg='white')
        self.salinButt.configure(state='disabled', bg='light gray')


class SRSA:
    def __init__(self,master):
        self.master = master
        self.bit = 5
        master.modeFieldCanvas.destroy()

        self.asciiKey = []

        for i in range(256):
            self.asciiKey.append(chr(i))

        master.modeFieldCanvas = tk.Canvas(master.canvas, relief='solid', borderwidth=0.5, bg='light blue')
        master.modeFieldCanvas.place(relwidth=1, relheight=0.9, rely=0.096)
        master.modeFieldCanvas.bind("<Button-1>", master.unfocus)
        master.modeFieldCanvas.bind("<Button-3>", master.unfocus)

        self.input = tk.Text(master.modeFieldCanvas, wrap='word',bg='white', borderwidth=0.5, relief='solid', font=('Arial', 12))
        self.input.place(relx=0.01, rely=0.01, relwidth=0.49, relheight=0.6)

        self.output = tk.Text(master.modeFieldCanvas, bg='white', fg='black', borderwidth=0.5, relief='solid',
                              font=('Arial', 12), state='disabled',wrap='word')  # textvariable=self.textOutput)
        self.output.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.6)

        self.labelMode = tk.Label(master.modeFieldCanvas, bg='white', fg='black',anchor = 'w', text='MODE : ', padx=10,font=master.font,borderwidth=0.5,relief='solid')
        self.labelMode.place(relx=0.01, rely=0.62, relwidth=0.98,relheight=0.09)

        self.encButt = tk.Button(master.modeFieldCanvas, bg='yellow', text='ENKRIPSI',borderwidth=0.5,relief='solid',state='disabled',command=self.enkripsi)
        self.encButt.place(relx=0.11,rely=0.63,relwidth=0.1,relheight=0.07)

        self.decButt = tk.Button(master.modeFieldCanvas, bg='white', text='DEKRIPSI', borderwidth=0.5, relief='solid',command=self.dekripsi)
        self.decButt.place(relx=0.22, rely=0.63, relwidth=0.1, relheight=0.07)

        self.salinButt = tk.Button(master.modeFieldCanvas, bg='white', text='SALIN', borderwidth=0.5, relief='solid',command = self.salinText)
        self.salinButt.place(relx=0.69, rely=0.63, relwidth=0.1, relheight=0.07)
        self.salinButt.bind("<Enter>",master.entered)
        self.salinButt.bind("<Leave>",master.leaves)

        self.simKeyLabel = tk.Label(master.modeFieldCanvas, bg='white', fg='black', anchor='w', text='''KUNCI PRIVAT: 
    (d,n)  ''', padx=5,pady=20,justify=tk.LEFT,font=("Consolas",12), borderwidth=0.5, relief='solid')
        self.simKeyLabel.place(relx=0.01, rely=0.72, relwidth=0.98, relheight=0.09*2)

        self.decKey = tk.Text(master.modeFieldCanvas, bg='light gray', borderwidth=0.5, relief='solid', font=('Consolas', 12),padx=10,pady=10,wrap='none',state='disabled')
        self.decKey.place(relx=0.17, rely=0.73, relwidth=0.5, relheight=0.07)
        self.nKey = tk.Text(master.modeFieldCanvas, bg='light gray', borderwidth=0.5, relief='solid',
                              font=('Consolas', 12), padx=10, pady=10, wrap='none',state='disabled')
        self.nKey.place(relx=0.17, rely=0.82, relwidth=0.5, relheight=0.07)

        self.simKeyButt = tk.Button(master.modeFieldCanvas, bg='white', text='PROSES!', borderwidth=0.5, relief='solid',command=self.proses)
        self.simKeyButt.place(relx=0.68, rely=0.73, relwidth=0.1, relheight=0.07)
        self.encryptedText = ''
        self.simKeyButt.bind("<Enter>", master.entered)
        self.simKeyButt.bind("<Leave>", master.leaves)

    def salinText(self):
        self.master.root.clipboard_clear()
        self.master.root.clipboard_append(' '.join(str(i) for i in self.encryptedText))
        self.master.root.clipboard_append('', type='STRING')

    def enkripsi(self):
        self.encButt.configure(state='disabled',bg='yellow')
        self.decButt.configure(state='normal',bg='white')
        self.decKey.configure(state='disabled',bg='light gray')
        self.nKey.configure(state='disabled',bg='light gray')
        self.input.configure(state='normal')
        self.input.delete(1.0,tk.END)
    def dekripsi(self):
        self.decButt.configure(state='disabled',bg='yellow')
        self.encButt.configure(state='normal',bg='white')
        self.decKey.configure(state='normal',bg='white')
        self.nKey.configure(state='normal',bg='white')
        self.input.configure(state='disabled')
        self.master.insert_to(self.input,"MASIH DALAM PROSES ^^")


    def proses(self):
        self.plainText = self.input.get("1.0","end-1c")

        if self.encButt.cget("state") == "disabled":
            self.encrypted = list(processes(self.plainText))
            self.encryptedText = [str(i) for i in self.encrypted[0]]
            self.master.insert_to(self.output, " ".join(self.encryptedText))
        else:
            try:
                self.d = int(self.decKey.get("1.0","end-1c"))
                self.n = int(self.nKey.get("1.0", "end-1c"))
            except ValueError:
                self.decKey.delete(1.0, tk.END)
                self.nKey.delete(1.0, tk.END)


class Dashboard:
    def __init__(self,root):
        self.root = root;

        self.font = ("Consolas bold", 14)

        self.canvas = tk.Canvas(self.root,height=600,width = 800,bg='white')
        self.canvas.pack()

        self.modePickCanvas = tk.Canvas(self.canvas,bg='white',relief='solid',borderwidth=0.5)
        self.modePickCanvas.place(relwidth=1,relheight=0.1)
        self.modeFieldCanvas = tk.Canvas(self.canvas,bg='white',relief='solid',borderwidth=0.5)
        self.modeFieldCanvas.place(relwidth=1,relheight=0.9,rely=0.096)
        self.modePickCanvas.bind("<Button-1>", self.unfocus)
        self.modePickCanvas.bind("<Button-3>", self.unfocus)
        self.modeFieldCanvas.bind("<Button-1>", self.unfocus)
        self.modeFieldCanvas.bind("<Button-3>", self.unfocus)

        self.modeList = [
            "CEK ISBN",
            "CAESAR CIPHER (alphanumeric)",
            "SIMPLE RSA"
        ]

        self.style = ttk.Style()
        self.style.configure("Custom.TCombobox", font = ('Arial',32), height =5)

        self.modePickerLabel = tk.Label(self.modePickCanvas,text='PILIH MODE : ',bg='white')
        self.modePickerLabel.place(relx=0.05,rely=0.5,relwidth=0.3,relheight=0.6,anchor='w')

        self.modePicker = ttk.Combobox(self.modePickCanvas,value = self.modeList,width=30,state='readonly',style="Custom.TCombobox")
        self.modePicker.current(2)
        self.modePicker.configure(height=100)
        self.modePicker.pack(pady=21,side='left',padx=200)
        self.modePicker.bind("<<ComboboxSelected>>", self.selecting)
        self.pickButt = tk.Button(self.modePickCanvas, bg='light gray',text='PILIH',borderwidth=0.5,relief='solid',command=self.picking,state='disabled')
        self.pickButt.place(relx=0.51,rely=0.25,relheight=0.5,relwidth=0.1)
        self.pickButt.bind("<ButtonPress-1>", self.buttPress)
        self.pickButt.bind("<Enter>",self.entered)
        self.pickButt.bind("<Leave>",self.leaves)
        self.pickButt.bind("<ButtonRelease-1>", self.buttRelease)
        self.pickButt.bind("<Button-1>",self.buttPress)

        self.modeGet = 'SIMPLE RSA'
        self.mode = SRSA(self)
        root.bind("<Configure>",self.comboboxUpdate)

    def comboboxUpdate(self,e):
        www = self.modePickCanvas.winfo_width() // 27
        hhh =  self.modePickCanvas.winfo_height() // 10
        self.modePicker.config(width=www, height=hhh)
    def selecting(self,e):
        self.pickButt.configure(state='normal',bg='white')
        if self.modePicker.get() == self.modeGet:
            self.pickButt.configure(state='disabled',bg='light gray')
    def picking(self):
        self.pickButt.configure(state='disabled',bg='light gray')
        self.modeGet = self.modePicker.get()
        if self.modePicker.get() == 'CEK ISBN':
            self.mode = ISBN(self)
        elif self.modePicker.get() == 'CAESAR CIPHER (alphanumeric)':
            self.mode = Caesar(self)
        elif self.modePicker.get() == 'SIMPLE RSA':
            self.mode = SRSA(self)
    def entered(self,e):
        e.widget.configure(bg="yellow")
    def leaves(self,e):
        e.widget.configure(bg="white")
        if e.widget.cget("state") == "disabled":
            e.widget.configure(bg="light gray")
    def buttPress(self,e):
        e.widget.configure(bg="yellow")
    def buttRelease(self,e):
        e.widget.configure(bg='white')
        if e.widget.cget("state") == "disabled":
            e.widget.configure(bg="light gray")
    def unfocus(self,e):
        e.widget.focus_set()

    def insert_to(self, widget,text):
        widget.configure(state='normal')
        widget.delete(1.0, tk.END)
        widget.insert("2.0", text+"\n")
        widget.configure(state='disabled')

    def salinText(self,text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.clipboard_append('', type='STRING')

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=800,height=600)

    app = Dashboard(root)

    app.root.mainloop()