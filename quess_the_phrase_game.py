import tkinter as tk
from tkinter import messagebox as mg
import random


class App:
    def __init__(self, root):
        self.button2 = None
        self.label1 = None
        self.label3 = None
        self.label2 = None
        self.button = None
        self.entry = None
        self.root = root
        self.fnt = "Arial 30"
        self.filename = "words.txt"
        self.words = []
        self.text = ''
        self.get_word_from_file()
        self.choose_words()
        self.widgets()

    def get_word_from_file(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            w = f.readlines()
        f.close()
        for i in w:
            i = i.strip()
            self.words.append(i)
        random.shuffle(self.words)
        print(self.words)

    def choose_words(self):
        self.text = random.choice(self.words)

    def widgets(self):
        shuffled_text = self.shuffle_text_and_words()
        self.label1 = tk.Label(self.root, text="Βρείτε την Φράση!!!!!", font=self.fnt)
        self.label2 = tk.Label(self.root, text=shuffled_text, font=self.fnt)
        self.label3 = tk.Label(self.root, text='', font=self.fnt)
        self.entry = tk.Entry(self.root, font=self.fnt, width=40, justify="center")
        self.button = tk.Button(self.root, text="Έλεγχος Απάντησης", font=self.fnt, command=self.check_answer)
        self.button2 = tk.Button(self.root, text="Έξοδος", font=self.fnt, command=self.exit_game)
        self.label1.pack(fill="both", expand=True)
        self.label2.pack(fill="both", expand=True)
        self.label3.pack(fill="both", expand=True)
        self.entry.pack(fill="both", expand=True)
        self.button.pack(fill="y", expand=True, side="left")
        self.button2.pack(fill="y", expand=True, side="right")

    def shuffle_text_and_words(self):
        puzzle = self.text.split()
        random.shuffle(puzzle)
        shuffled_text = ''
        for i in puzzle:
            shuffled_text += ''.join(random.sample(i, len(i))) + ' '
        return shuffled_text

    def check_answer(self):
        t = self.entry.get()
        if t == self.text:
            msg_box = mg.askquestion('Συγχαρητήρια ', 'Συγχαρητήρια Κερδίσατε. Θέλετε να ξανά παίξετε???')
            if msg_box == 'yes':
                r.destroy()
                r2 = tk.Tk()
                r2.title("Βρείτε την Φράση!!!!!!")
                App(r2)
                r2.mainloop()
            else:
                self.exit_game()
        else:
            resp = "Όχι δεν τα κατάφερες ξαναδοκίμασε"
            self.label3.config(text=resp)

    def exit_game(self):
        self.root.destroy()


r = tk.Tk()
r.title("Βρείτε την Φράση!!!!!!")
App(r)
r.mainloop()
