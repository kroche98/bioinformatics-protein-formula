import tkinter as tk
import proteinformula
import string

class ProteinFormulaApp():
    def __init__(self, master):
        self.master = master
        master.title("Protein Formula Calculator")

        self.create_widgets(master)

    def create_widgets(self, master):
        # Welcome message
        self.welcome_message = tk.Label(master, text="Welcome to the Protein Formula Calculator!\nSelect a mode, and enter a sequence\nto calculate the chemical formula of a protein.")
        self.welcome_message.pack()

        # Radio button to select entry mode
        modes = [("1-letter amino acid codes", "aa1"), ("3-letter amino acid codes", "aa3"), ("DNA sequence", "dna"), ("RNA sequence", "rna")]
        self.mode_var = tk.StringVar(value='aa1') # default mode is 1-letter amino acid codes
        for text, mode in modes:
            b = tk.Radiobutton(master, text=text, variable=self.mode_var, value=mode)
            b.pack()

        # Entry field
        self.entry_field = tk.Entry(master)
        self.entry_field.pack()

        # Submit button
        self.submit_button = tk.Button(master, text='Submit', command=self.update_result)
        self.submit_button.pack()

        # Result field
        self.result_field = tk.Entry(master, font="Arial 16", width=16, justify=tk.CENTER, state='readonly')
        self.result_field.pack()
    
    def update_result(self):
        # get input text and remove whitespace
        raw_text = ''.join(ch for ch in self.entry_field.get() if ch not in string.whitespace)
        
        # compute the formula
        formula = proteinformula.compute_formula(raw_text, mode=self.mode_var.get())
        formula_text = proteinformula.formula_to_string(formula)

        # use fancy Unicode subscripts for the numbers
        trantab = str.maketrans(''.join(str(i) for i in range(10)), ''.join(chr(0x2080 + i) for i in range(10)))
        formula_text = formula_text.translate(trantab)
        
        # update the display box
        self.result_field.config(state=tk.NORMAL)
        self.result_field.delete(0, tk.END)
        self.result_field.insert(0, formula_text)
        self.result_field.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    protein_formula_app = ProteinFormulaApp(root)
    root.mainloop()
