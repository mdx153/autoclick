import pyautogui #pip install pyautogui
import keyboard #pip install keyboard
import time 
import random 
from tkinter import * #pip install tk ou tkinter
from tkinter import messagebox

permitirClick = False
tempoRelativo = 0

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.permiteExecutar = False

        self.primeroContainer = Frame(master)
        self.primeroContainer["pady"] = 10
        self.primeroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeroContainer, text="Auto Click")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabelTempo = Label(self.segundoContainer, text="Tempo em (s)", font=self.fontePadrao)
        self.nomeLabelTempo.pack(side=LEFT)

        self.tempo = Entry(self.segundoContainer, textvariable= StringVar(None, value=10))
        self.tempo["width"] = 20
        self.tempo["font"] = self.fontePadrao
        self.tempo.pack(side=LEFT)

        self.mensagem = Label(self.primeroContainer, text='Desativado', font=self.fontePadrao, fg="#F50A0A")
        self.mensagem.pack()

        self.btnAutoClick = Button(self.terceiroContainer, )
        self.btnAutoClick["text"] = "Executar"
        self.btnAutoClick["font"] = ("Calibri", "8")
        self.btnAutoClick["width"] = 12
        self.btnAutoClick["command"] = self.permiteExecutarClick
        self.btnAutoClick.pack()

    def permiteExecutarClick(self):
        global permitirClick
        global tempoRelativo
        if permitirClick:
            permitirClick = False
            self.mensagem['text'] = "Desativado"
            self.mensagem['fg'] = '#F50A0A'
        else:
            tempo = self.tempo.get().strip()
            if tempo == None and tempo == '':
                messagebox.showerror("Error","Campo 'Tempo em (s)' vazio")
                permitirClick = False
                self.mensagem['text'] = "Desativado"
                self.mensagem['fg'] = '#F50A0A'
                exit
                
            if not self.tempo.get().isnumeric():
                messagebox.showerror("Error","Campo 'Tempo em (s)' inválido")
                return

            tempoRelativo = int(self.tempo.get())  
            permitirClick = True
            self.mensagem['text'] = "Ativado"
            self.mensagem['fg'] = '#3EA436'

               
root = Tk() 
root.iconbitmap('.\\AutomatizadorClick\\1298385.ico')
root.title("Cliques automático")
root.minsize(500,100)

def executarAutoClick():
    global permitirClick
    global tempoRelativo

    if keyboard.is_pressed('esc'):
        return
    
    if not permitirClick:
        return

    time.sleep(tempoRelativo)
    pyautogui.click(x=random.randint(0,500), y=random.randint(0,500))
    root.after(5000, executarAutoClick)

root.after(5000, executarAutoClick)
root.eval('tk::PlaceWindow . center')

Application(root)
root.mainloop()