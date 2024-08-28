import tkinter as tk
from tkinter import messagebox

class ContCreciente(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.contador = 0
        self.initUI()
        
    def initUI(self):
        self.title("ContCreciente")
        
        # Configurando la etiqueta
        self.label = tk.Label(self, text="Contador", font=("Arial", 16, "bold"), fg="Black")
        self.label.pack(pady=10)
        
        # Configurando el lineEdit (usando Entry en Tkinter)
        self.line_edit = tk.Entry(self, font=("Times New Roman", 14), fg="orange", bg="orange", justify="center")
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")
        self.line_edit.pack(pady=10)
        
        # Configurando el botón
        self.button = tk.Button(self, text="+", font=("Verdana", 12), bg="grey", fg="white", command=self.incrementar_contador)
        self.button.pack(pady=10)
        
    def incrementar_contador(self):
        self.contador += 1
        self.line_edit.config(state="normal")  # Habilitar para actualizar el valor
        self.line_edit.delete(0, tk.END)
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")  # Deshabilitar de nuevo
        
        if self.contador == 10:
            self.mostrar_mensaje()
        elif self.contador == 20:
            self.mostrar_mensaje2()
        

    def mostrar_mensaje(self):
        messagebox.showinfo("Contador", "¡El contador ha llegado a 10!")
    def mostrar_mensaje2(self):
        messagebox.showinfo("Contador", "¡El contador ha llegado a 20!")
    

if __name__ == "__main__":
    app = ContCreciente()
    app.mainloop()