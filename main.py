from tkinter import *

root = Tk()
class imc():
    def __init__(self):
        self.root = root
        self.janela()
        self.desenho()
       
        root.mainloop()
    def janela(self):
        self.root.title("Calculadora do índice de massa corporal (IMC)")
        self.root.configure(background= '#B0C4DE')
        self.root.geometry("450x150")
        self.root.resizable(True, True)
    def desenho(self):
        self.quilos = DoubleVar()
        self.lb_quilos = Label(text='Peso (em Kg)',
                                       font=('Verdana', '8', 'bold'),
                                       bg='#D3D3D3', fg='#000000')
        self.lb_quilos.place(relx=0.2, rely=0.05, relwidth=0.35,
                                     relheight=0.1)
        self.input_quilos = Entry(textvariable=self.quilos)
        self.input_quilos.place(relx=0.6, rely=0.05, relwidth=0.2,
                                        relheight=0.1)

        self.altura = DoubleVar()
        self.lb_altura = Label(text='Altura (em metros) ',
                                       font=('Verdana', '8', 'bold'),
                                    bg='#D3D3D3', fg='#000000')
        self.lb_altura.place(relx=0.2, rely=0.2,
                                  relwidth=0.35, relheight=0.1)
        self.input_altura = Entry(textvariable=self.altura)
        self.input_altura.place(relx=0.6, rely=0.2,
                                     relwidth=0.2, relheight=0.1)

        self.bt_calcular = Button( text='Calcular o IMC',
                                bg='#808080', fg='#F8F8FF',
                                   font=("verdana", 10, "bold"),
                                   command = self.butaoclick1)
        self.bt_calcular.place(relx=0.3, rely=0.4, relwidth=0.4,
                               relheight=0.17)
        # Resultado
        self.imcfinal = StringVar()
        self.imcfinal1 = Label(textvariable=self.imcfinal)

        self.resultado1 = Label(textvariable=self.imcfinal)
        self.resultado1.place(relx=0.1, rely=0.65, relwidth=0.8,relheight=0.2)