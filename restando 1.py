import tkinter as tk

class ContDecreciente:
    def __init__(self, root):
        self.root = root
        self.root.title("ContDecreciente")
        
        self.contador = 88  # El contador empieza en 88
        
        # Creando los componentes
        self.label = tk.Label(root, text="Contador", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.line_edit = tk.Entry(root, font=("Arial", 14), justify="center")
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")
        self.line_edit.pack(pady=10)
        
        self.button = tk.Button(root, text="-", font=("Arial", 14), command=self.decrementar_contador)
        self.button.pack(pady=10)
    
    def decrementar_contador(self):
        self.contador -= 1
        self.line_edit.config(state="normal")  # Habilitar para actualizar el valor
        self.line_edit.delete(0, tk.END)
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")  # Deshabilitar de nuevo

if __name__ == "__main__":
    root = tk.Tk()
    app = ContDecreciente(root)
    root.mainloop()