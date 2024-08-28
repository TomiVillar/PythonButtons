import tkinter as tk
import random

class Peliculas(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.config(bg="orange")
        self.n = 1
        self.initUI()

    def initUI(self):
        self.labelp = tk.Label(self, text= "Elegi un parametro de numeros",font=("Arial",16), fg= "black", bg= "orange")
        self.labelp.grid(row= 0, column= 0, padx= 0, pady= 0)

        self.labeln1= tk.Label(self, text= "Numero 1",font=("Arial",16), fg= "black", bg= "orange")
        self.labeln1.grid(row= 1, column= 0, padx= 0, pady= 0)

        self.labeln2 = tk.Label(self, text= "Numero 2",font=("Arial",16), fg= "black", bg= "orange")
        self.labeln2.grid(row= 2, column= 0, padx= 0, pady= 0)

        self.labelng = tk.Label(self, text= "Numero Generado",font=("Arial",16), fg= "black", bg= "orange")
        self.labelng.grid(row= 4, column= 0, padx= 0, pady= 0)

        self.spinbox_1 = tk.Spinbox(self, from_=0, to=100, font=("Times new Roman", 14, "bold"),
                                    fg="orange",bg="black", width= 5)
        self.spinbox_1.grid(row= 1, column=1, padx=0, pady=0)

        self.spinbox_2 = tk.Spinbox(self, from_=0, to=100, font=("Times new Roman", 14, "bold"),
                                    fg="orange",bg="black", width= 5)
        self.spinbox_2.grid(row= 2, column=1, padx=40, pady=0)

        self.line_edit= tk.Entry(self,font=("Times new Roman", 14, "bold"),fg="orange",bg="black", width= 18)
        self.line_edit.config(state="readonly")
        self.line_edit.grid(row=4, column=1, padx=10, pady=10)

        self.button_G =tk.Button(self, text="Generar",command=self.Generar_numero, font=("arial", 16 ,"bold"), bg="black", fg="orange")
        self.button_G.grid(row=3, column=0 , padx=0, pady=0)

    def Generar_numero(self):
        num1 = int(self.spinbox_1.get())
        num2 = int(self.spinbox_2.get())
        if num1 <= num2:
            random_number = random.randint(num1, num2)
            self.line_edit.config(state="normal")  # Hacer el Entry editable temporalmente
            self.line_edit.delete(0, tk.END)  # Borrar el texto existente
            self.line_edit.insert(0, str(random_number))  # Insertar el número generado
            self.line_edit.config(state="readonly")
        else:
            self.line_edit.config(state="normal")
            self.line_edit.delete(0, tk.END)
            self.line_edit.insert(0, "Error: Rango Inválido")
            self.line_edit.config(state="readonly")
if __name__ == "__main__":
    app =Peliculas()
    app.mainloop()
