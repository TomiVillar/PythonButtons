import tkinter as tk
import math

class FactorialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Factorial")
        root.config(bg="#b5b5b5")
        self.n = 1
        
        # Creando los componentes
        self.label_n = tk.Label(root, text="n", font=("Arial", 14),fg= "orange")
        self.label_n.pack(pady=5)
        
        self.line_edit_n = tk.Entry(root, font=("Arial", 14), fg= "orange", justify="center")
        self.line_edit_n.insert(0, str(self.n))
        self.line_edit_n.config(state="readonly")
        self.line_edit_n.pack(pady=5)
        
        self.label_fact = tk.Label(root, text="Factorial (n)", font=("Arial", 14), fg= "orange")
        self.label_fact.pack(pady=5)
        
        self.line_edit_fact = tk.Entry(root, font=("Arial", 14), fg= "orange", justify="center")
        self.line_edit_fact.insert(0, str(math.factorial(self.n)))
        self.line_edit_fact.config(state="readonly")
        self.line_edit_fact.pack(pady=5)
        
        self.button = tk.Button(root, text="Siguiente", font=("Arial", 14), fg= "red", command=self.siguiente)
        self.button.pack(pady=10)
    
    def siguiente(self):
        self.n += 1
        self.line_edit_n.config(state="normal")
        self.line_edit_n.delete(0, tk.END)
        self.line_edit_n.insert(0, str(self.n))
        self.line_edit_n.config(state="readonly")
        
        self.line_edit_fact.config(state="normal")
        self.line_edit_fact.delete(0, tk.END)
        self.line_edit_fact.insert(0, str(math.factorial(self.n)))
        self.line_edit_fact.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = FactorialApp(root)
    root.mainloop()