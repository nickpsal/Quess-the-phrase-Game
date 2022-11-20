import tkinter as tk
from tkinter import messagebox as mg
import random


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Βρείτε την Φράση!!!!!! V2.0")
        self.root.configure(bg="grey")
        self.root.resizable(False, False)
        self.fnt = "Arial 30"
        self.filename = "words.txt"
        self.words = []
        self.text = ''
        self.label3 = None
        self.entry = None
        self.get_word_from_file()
        random.shuffle(self.words)
        print(self.words)
        self.choose_words()
        self.shuffled_text = self.shuffle_text_and_words()
        print(self.text)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self.root, bg="grey")
        label1 = tk.Label(frame1, text="Βρείτε την Φράση!!!!!", font=self.fnt, bg="grey")
        label2 = tk.Label(frame1, text=self.shuffled_text, font=self.fnt, bg="grey")
        self.label3 = tk.Label(frame1, text='', font=self.fnt, bg="grey")
        self.entry = tk.Entry(frame1, font=self.fnt, width=40, justify="center", bg="grey")
        frame2 = tk.Frame(self.root, bg="grey")
        button = tk.Button(frame2, text="Έλεγχος Απάντησης", font=self.fnt, command=self.check_answer,
                           bg="grey")
        button2 = tk.Button(frame2, text="Έξοδος", font=self.fnt, command=self.exit_game, bg="grey")
        button3 = tk.Button(frame2, text="Πληροφορίες", font=self.fnt, command=self.show_info, bg="grey")
        frame1.pack(fill="both", expand=True, side="top", padx=5, pady=5)
        frame2.pack(fill="both", expand=True, side="bottom", padx=5, pady=5)
        label1.pack(fill="both", expand=True)
        label2.pack(fill="both", expand=True)
        self.label3.pack(fill="both", expand=True)
        self.entry.pack(fill="both", expand=True)
        button.pack(fill="y", expand=True, side="left")
        button2.pack(fill="y", expand=True, side="right")
        button3.pack(fill="y", expand=True, side="left")

    def get_word_from_file(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            w = f.readlines()
        f.close()
        for i in w:
            i = i.strip()
            self.words.append(i)

    def choose_words(self):
        self.text = random.choice(self.words)

    def shuffle_text_and_words(self):
        puzzle = self.text.split()
        random.shuffle(puzzle)
        shuffled_text = ''
        for i in puzzle:
            shuffled_text += ''.join(random.sample(i, len(i))) + ' '
        return shuffled_text

    def check_answer(self):
        if self.entry.get() == self.text:
            msg_box = mg.askquestion('Συγχαρητήρια ', 'Συγχαρητήρια Κερδίσατε. Θέλετε να ξανά παίξετε???')
            if msg_box == 'yes':
                self.root.destroy()
                r2 = tk.Tk()
                r2.title("Βρείτε την Φράση!!!!!!")
                App(r2)
                r2.mainloop()
            else:
                self.root.destroy()
        else:
            resp = "Όχι δεν τα κατάφερες ξαναδοκίμασε"
            self.label3.config(text=resp)

    def exit_game(self):
        self.root.destroy()

    @staticmethod
    def show_info():
        info_box = mg.showinfo("Πληροφορίες", '''Παιχνίδι Βρείτε την Φράση  Έκδοση V 2.0
Προγραμματιστής : Ψαλτάκης Νικόλαος
Φτιάχτηκε με την Python Έκδοση 3.11.0''')


r = tk.Tk()
App(r)
r.mainloop()
