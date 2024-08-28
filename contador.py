import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")
        
        self.contador = 0  # Inicializa el contador en 0
        
        # Creando los componentes
        self.label = tk.Label(root, text="Contador", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.line_edit = tk.Entry(root, font=("Arial", 14), justify="center")
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")
        self.line_edit.pack(pady=10)
        
        self.button_up = tk.Button(root, text="Count Up", font=("Arial", 14), command=self.incrementar_contador)
        self.button_up.pack(side="left", padx=10)
        
        self.button_down = tk.Button(root, text="Count Down", font=("Arial", 14), command=self.decrementar_contador)
        self.button_down.pack(side="left", padx=10)
        
        self.button_reset = tk.Button(root, text="Reset", font=("Arial", 14), command=self.resetear_contador)
        self.button_reset.pack(side="left", padx=10)
    
    def incrementar_contador(self):
        self.contador += 1
        self.actualizar_line_edit()
        
    def decrementar_contador(self):
        self.contador -= 1
        self.actualizar_line_edit()
    
    def resetear_contador(self):
        self.contador = 0
        self.actualizar_line_edit()
    
    def actualizar_line_edit(self):
        self.line_edit.config(state="normal")  # Habilitar para actualizar el valor
        self.line_edit.delete(0, tk.END)
        self.line_edit.insert(0, str(self.contador))
        self.line_edit.config(state="readonly")  # Deshabilitar de nuevo

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
