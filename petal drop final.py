from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

#different categories
def fruits():
    fruits = ['apple', 'banana', 'cherry', 'orange', 'grape', 'watermelon', 'kiwi', 'strawberry']
    return random.choice(fruits)

def programming():
    programming = ["list","string","dictionary","syntax","variable","identifier","function"]
    return random.choice(programming)

def animals():
    animals = ["horse","koala","elephant","duck","hippopotamus","crocodile","lion","cheetah"]
    return random.choice(animals)

class PetalGame:
    def __init__(self, master,score_label):
        self.master = master #creating a reference to make widgets like buttons,labels etc
        self.word_to_guess = "" #setting default word to guess as empty
        self.guessed_letters = set() #empty set of guessed letters
        self.attempts = 5 #no. of guesses

        self.word_label=""
        self.label_category = Label(master, text="Choose a category:",
                                    font=("Courier",20),bg="mediumpurple1",
                                    padx=10,pady=10)
        self.label_category.place(x=250,y=1)

        #buttons corresponding to its respective category
        self.fruits_button = Button(master, text="Fruits", command=self.select_fruit, width=15, height=2)
        self.fruits_button.place(x=200,y=45)

        self.programming_button = Button(master, text="Programming",
                                         command=self.select_programming,
                                         width=15, height=2)
        self.programming_button.place(x=345,y=45)

        self.animals_button = Button(master, text="Animals", command=self.select_animal,
                                     width = 15, height=2)
        self.animals_button.place(x=492,y=45)

        #canvas to store the petal images
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.place(x=200, y=100)

        self.load_images()
        self.current_petal_image = self.petal_images[self.attempts]
        self.update_petals()

        #score count
        self.score = 0
        self.score_label=score_label

        #word with the guessed letters
        self.word_label = Label(master, text=self.display_word(),font=("Calibri", 12),width=20,height=1)
        self.word_label.place(x=325,y=512)

        #guess box
        self.guess_entry = Entry(master,font=("Calibri 14"), width=5)
        self.guess_entry.place(x=353,y=542)

        #guess button
        self.guess_button = Button(master, text="Guess",font=("Calibri",10),command=self.make_guess)
        self.guess_button.place(x=422,y=543)

    def load_images(self):
        #dictionary storing no. of petals corresponding to no. of petals
        self.petal_images = {5: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_5.png"),
                             4: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_4.png"),
                             3: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_3.png"),
                             2: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_2.png"),
                             1: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_1.png"),
                             0: PhotoImage(file="C:\\Users\\Khalilur Rahman\\petal_0.png")}
        
        self.petal_item = None #created to manage the canvas

    def update_petals(self):
        if self.petal_item is not None:
            self.canvas.delete(self.petal_item) #deleting image to replace with an updated image
        petal_image = self.petal_images.get(self.attempts)

        if petal_image:#checks if it exists-has non empty value
            self.petal_item = self.canvas.create_image(0,0,anchor=NW,image=petal_image)
            self.canvas.update() #update image

    #call function to get a word from corresponding category
    def select_fruit(self):
        self.word_to_guess = fruits()
        self.reset_game()

    def select_programming(self):
        self.word_to_guess = programming()
        self.reset_game()

    def select_animal(self):
        self.word_to_guess = animals()
        self.reset_game()

    #called to reset game when category button clicked
    def reset_game(self):
        self.guessed_letters = set()
        self.attempts = 5
        self.word_label.config(text=self.display_word())
        self.update_petals()

    def display_word(self):
        displayed_word = ''
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '_ '
        return displayed_word

    def make_guess(self):
        guess = self.guess_entry.get().lower() #doesnt matter if guess is in uppercase as it converts to lowercase
        self.guess_entry.delete(0, END) #clears text the player entered in guess box, preparing it for next guess

        if len(guess)!=1 or not guess.isalpha(): #if other characters instead of letter entered
            messagebox.showinfo("INVALID GUESS", "Please enter a single letter.")
            return

        if guess in self.guessed_letters: #same letter guessed
            messagebox.showinfo("DUPLICATE GUESS", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess not in self.word_to_guess:
            self.attempts -= 1 #attempts reduced by one with each guess
            self.update_petals()  #update canvas image
            self.word_label.config(text=self.display_word()) #updating the text 

        if self.attempts == 0: #no guess left
            messagebox.showinfo("GAME OVER",
                                "Sorry, you ran out of attempts. The word was: {}".format(self.word_to_guess))
            self.master.destroy()

        else:
            self.word_label.config(text=self.display_word())  #update displayed word

        if self.display_word().replace(' ', '') == self.word_to_guess: #checks if guessed word is equal to original
            messagebox.showinfo("Congratulations!", "You guessed the word: {}".format(self.word_to_guess))
            self.score+=10
            print(self.score)
            self.word_label.config(text=self.display_word()) #update word
            self.score_label.config(text="Score: {}".format(self.score))

def open_Petal_Game(): #does not open if name is not entered
    global n
    if n!="":
        Petal_Game = Toplevel(prgm)
        Petal_Game.title("PETAL DROP: PLAY")
        Petal_Game.geometry("800x700")
        Petal_Game.resizable(False,False)
        Petal_Game.configure(bg="mediumpurple1")
        player = Label(Petal_Game,text="Player: "+n,
                       font=('Helvetica 17 bold'),
                       bg="medium purple1",
                       padx=10,pady=10).place(x=1,y=1)
        print ("Opened")

        score_label = Label(Petal_Game, text="Score: 0", font=("Calibri", 14),width=15)
        score_label.place(x=30,y=510)
        game = PetalGame(Petal_Game, score_label)

if __name__ == "__main__": #main window
    prgm = Tk()
    prgm.title("PETAL DROP")
    prgm.geometry("700x255")
    prgm.configure(bg="LightBlue")
    prgm.resizable(False,False)
    
    l=Label(text="PETAL DROP",
            font=("Courier",50),
            padx=10,pady=10)
    l.grid(row=0,column=1)
    l.configure(bg="LightBlue")

    name=StringVar()

    n=None

    def entername():
        global prgm,n
        n=name.get() #recieves name entered
        if n=="": #no name
            n0=Label(text="Please enter a name.",
                     font=("Courier",14))
            n0.grid(row=3,column=1)
            n0.configure(bg="LightBlue")
        else:
            nl=Label(text="The player is: "+n,
                     font=("Courier",14),
                     width=30)
            nl.grid(row=3,column=1)
            nl.configure(bg="LightBlue")
            name.set("")

    def credit():
        credit_page = Toplevel(prgm)
        credit_page.title("Credit Page")
        credit_page.geometry("400x235")
        credit_page.resizable(False,False)
        credit_page.configure(bg="DimGrey")

        doneby = Label(credit_page,text="PROJECT DONE BY:",font=('Helvetica 17 bold'),
                       bg="DimGrey",padx=10,pady=10).place(x=70,y=1)
        names = Label(credit_page,text="Nasrin Rahman 12-B\n Sauda Mohammed 12-B",
                      font=("Helvetica",12),bg="Grey").place(x=105,y=40)
        b = Label(credit_page,text="BIBLIOGRAPHY",font=("Helvetica 17 bold"), bg="DimGrey").place(x=95,y=100)
        links = Label(credit_page,text="""https://www.pythontutorial.net/tkinter/
https://github.com/
https://www.geeksforgeeks.org/
https://python-forum.io
https://medium.com/p/fedda58741b""",
        font=("Helvetica",12),bg="Grey").place(x=60,y=130)

    #name from user
    name_l=Label(prgm,text="Player Name:",
                 font=("Hellvetica",14,'bold'),
                 padx=10, pady=10)
    name_e=Entry(prgm,textvariable=name,
                 font=("Hellvetica",14,'normal'))
    playbtn=Button(prgm,text="Play!",font=("Calibri",14),
                   command=lambda:([entername(),open_Petal_Game()])) #lambda helps to call mulitple fns
    creditsbtn=Button(prgm,text="Credits",font=("Calibri",14),
                     command=credit)

    name_l.grid(row=1,column=0)
    name_l.configure(bg="LightBlue")
    name_e.grid(row=1,column=1)
    playbtn.grid(row=2,column=1)
    creditsbtn.place(x=323,y=200)

