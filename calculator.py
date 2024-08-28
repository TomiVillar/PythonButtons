import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Creando los componentes
        self.label_1 = tk.Label(root, text="Primer número", font=("Arial", 12))
        self.label_1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.label_2 = tk.Label(root, text="Segundo número", font=("Arial", 12))
        self.label_2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.label_resultado = tk.Label(root, text="Resultado", font=("Arial", 12))
        self.label_resultado.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        
        self.entry_1 = tk.Entry(root, font=("Arial", 12))
        self.entry_1.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
        
        self.entry_2 = tk.Entry(root, font=("Arial", 12))
        self.entry_2.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="w")
        
        self.entry_resultado = tk.Entry(root, font=("Arial", 12))
        self.entry_resultado.grid(row=2, column=1, padx=10, pady=5, columnspan=2)
        self.entry_resultado.config(state="readonly")
        
        # Botones de operación
        self.button_add = tk.Button(root, text="+", font=("Arial", 12), command=self.sumar)
        self.button_add.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        
        self.button_subtract = tk.Button(root, text="-", font=("Arial", 12), command=self.restar)
        self.button_subtract.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
        
        self.button_multiply = tk.Button(root, text="*", font=("Arial", 12), command=self.multiplicar)
        self.button_multiply.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
        
        self.button_divide = tk.Button(root, text="/", font=("Arial", 12), command=self.dividir)
        self.button_divide.grid(row=3, column=3, padx=10, pady=5, sticky="nsew")
        
        self.button_mod = tk.Button(root, text="%", font=("Arial", 12), command=self.modulo)
        self.button_mod.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
        
        self.button_clear = tk.Button(root, text="CLEAR", font=("Arial", 12), command=self.limpiar)
        self.button_clear.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="nsew")
        
        # Configurando el comportamiento de redimensionamiento
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_rowconfigure(4, weight=1)

    def sumar(self):
        try:
            num1 = float(self.entry_1.get())
            num2 = float(self.entry_2.get())
            resultado = num1 + num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
    
    def restar(self):
        try:
            num1 = float(self.entry_1.get())
            num2 = float(self.entry_2.get())
            resultado = num1 - num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
    
    def multiplicar(self):
        try:
            num1 = float(self.entry_1.get())
            num2 = float(self.entry_2.get())
            resultado = num1 * num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
    
    def dividir(self):
        try:
            num1 = float(self.entry_1.get())
            num2 = float(self.entry_2.get())
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ZeroDivisionError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
    
    def modulo(self):
        try:
            num1 = float(self.entry_1.get())
            num2 = float(self.entry_2.get())
            resultado = num1 % num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")
    
    def limpiar(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()