import tkinter as tk
import random


class App:
    def __init__(self, root):
        self.button = None
        self.entry = None
        self.label3 = None
        self.label2 = None
        self.label = None
        self.f = None
        self.root = root
        self.fnt = "Arial 30"
        self.text = "Καλησπέρα απο την Python"
        self.widgets()

    def widgets(self):
        shuffled_text = self.shuffle_text_and_words()
        self.label = tk.Label(self.root, text="Βρείτε την Φράση!!!!!", font=self.fnt)
        self.label2 = tk.Label(self.root, text=shuffled_text, font=self.fnt)
        self.label3 = tk.Label(self.root, text='', font=self.fnt)
        self.entry = tk.Entry(self.root, font=self.fnt, width=40, justify="center")
        self.button = tk.Button(self.root, text="Έλεγχος Απάντησης", font=self.fnt, command=self.check_answer)
        self.label.pack(fill="both", expand=True)
        self.label2.pack(fill="both", expand=True)
        self.label3.pack(fill="both", expand=True)
        self.entry.pack(fill="both", expand=True)
        self.button.pack(fill="both", expand=True)

    def shuffle_text_and_words(self):
        puzzle = []
        t = ''
        self.text += ' '
        for i in self.text:
            if i != ' ':
                t += i
            else:
                puzzle.append(t)
                t = ''
        random.shuffle(puzzle)
        shuffled_text = ''
        for i in puzzle:
            shuffled_text += ''.join(random.sample(i, len(i))) + ' '
        return shuffled_text

    def check_answer(self):
        t = self.entry.get()
        if t == self.text:
            resp = "Συγχαρητήρια το βρήκες"
        else:
            resp = "Όχι δεν τα κατάφερες ξαναδοκίμασε"
        self.label3.config(text=resp)


r = tk.Tk()
r.title("Βρείτε την Φράση!!!!!!")
App(r)
r.mainloop()
