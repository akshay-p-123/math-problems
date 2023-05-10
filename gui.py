import tkinter as tk
from tkinter import ttk
from tkinter import *
import math
import random as rand
import leaderboard as lb


username = ""

#list of all username and password combinations
user_pass_list = []

question_type = ""
no_questions = 0
correct_answers = 0
score = 0

#fonts to be used
title_font = ('Futura', 32, 'bold')
other_font = ('Comic Sans MS', 20)
text_box_font = ("Comic Sans MS", 8)




#creates the window and controls all of the frames
class Controller(tk.Tk):
    def __init__(self, file, *args, **kwargs):

        #initializing the window
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("720x510")
        self.title("Math Problems")
        self.container = tk.Frame(self, bg="#EADB18")
        self.container.pack(side="top", fill="both", expand = True)
           
        self.frames = {}

        #initializes the frames
        frames_tuple = (Frame_Login, Frame_Welcome, Frame_Start)
        for i in frames_tuple:
            frame = i(self.container, self) 
            self.frames[i] = frame
            
        self.show_frame(Frame_Login)

        #reads in the file of username-password combinations
        self.file = file
        for line in file:
            user_pass_list.append(line)
    
    

    def show_frame(self, type):
        f = self.frames[type]
        f.grid(row=0, column=0, sticky="news")
        self.container.tkraise()
        

    def init_frame_questions(self):
        frame = Frame_Questions(self.container, self)
        self.frames[Frame_Questions] = frame
        frame.grid(row=0, column=0, sticky="news")
        

    def init_frame_leaderboard(self):
        frame = Frame_Leaderboard(self.container, self)
        self.frames[Frame_Leaderboard] = frame
        frame.grid(row=0, column=0, sticky="news")
        


        

#frame to login
class Frame_Login(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        
        #adds background image
        self.photo = PhotoImage(file="background.png")
        self.bg_panel = ttk.Label(self, image=self.photo)
        self.bg_panel.place(x=0, y=0)   


        #creates frame components
        self.login_title = ttk.Label(self,text='Login',font=title_font, background="#F3A89C") #light orange
        self.login_title.grid(column=2, row=1, sticky=S, pady=50)

        self.lbl_username = ttk.Label(self,text='Username:', font=other_font, background="#ffffe0") #yellow
        self.lbl_username.grid(column=1, row=2, sticky =NSEW, pady=50, padx=5)

        self.ent_username = ttk.Entry(self, width=93)
        self.ent_username.grid(column=2, row=2, sticky =NSEW, columnspan=2, pady=50, padx=5)

        self.lbl_pass = ttk.Label(self,text="Password:", font=other_font, background="#ffffe0") #yellow
        self.lbl_pass.grid(column=1, row=3, sticky =NSEW, padx=5, pady=45)

        self.ent_pass = ttk.Entry(self, show="*", width=93)
        self.ent_pass.grid(column=2, row=3, sticky =NSEW, columnspan=2, pady=45, padx=5)

        self.error_label = ttk.Label(self, text="Sorry, your username or password is incorrect.", justify=tk.LEFT, background="#F3A89C") #light orange
        self.error_label.grid(column=1, row=5, sticky=NSEW)
        self.error_label.grid_forget()

        self.subButton = tk.Button(self,text='Login', width=79, height=2, background="#F3A89C") #light orange
        self.subButton.grid(column=2, row=4, sticky = NSEW, padx=5, pady=11)
        self.subButton.config(command=self.check_auth)

    #command for subButton
    #checks if login credentials are correct
    def check_auth(self):
        global username
        user_username = self.ent_username.get()
        password = self.ent_pass.get()
        combo = f"{user_username} {password}\n"
        for i in range(len(user_pass_list)-1):
            if (combo == user_pass_list[i]):
                self.grid_forget()
                self.controller.show_frame(Frame_Welcome)
                username = user_username
                break
        self.error_label.grid(column=2, row=5, sticky=NSEW)



#welcome frame
class Frame_Welcome(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #creates background image
        self.photo = PhotoImage(file="background.png")
        self.bg_panel = ttk.Label(self, image=self.photo)
        self.bg_panel.place(x=0, y=0)   
        
        #creates frame components
        self.welcome = ttk.Label(self, text="Welcome!", font=title_font, background='#ffffe0').pack(fill="both", padx=260, pady=60)

        self.start_button = tk.Button(self, text="Start", font=other_font, background="#F6C5B6")
        self.start_button.pack(fill="both", padx=260, pady=50)
        self.start_button.config(command=self.start)
        self.leaderboard_button = tk.Button(self, text="Leaderboard", font=other_font, background="#F6C5B6")
        self.leaderboard_button.pack(fill="both", padx=260, pady=50)
        self.leaderboard_button.config(command=self.show_leaderboard)
        self.grid_forget()

    #command for start_button
    #shows start frame
    def start(self):
        self.grid_forget()
        self.controller.show_frame(Frame_Start)
    
    #command for leaderboard_button
    #initializes and shows leaderboard frame
    def show_leaderboard(self):
        self.grid_forget()
        self.controller.init_frame_leaderboard()
        self.controller.show_frame(Frame_Leaderboard)


#start frame
class Frame_Start(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg="#EADB18")
        self.controller = controller

        #creates frame components
        self.photo = PhotoImage(file="background.png")
        self.bg_panel = ttk.Label(self, image=self.photo)
        self.bg_panel.place(x=0, y=0) 

        self.start_label = ttk.Label(self, text="Start", font=title_font, background="#F3A89C").grid(row=0, column=0, sticky="news", padx=75, pady=60) #light orange

        self.dropdown_label = ttk.Label(self, text="Question type", font=other_font, background="#FDF6E7").grid(row=1, column=0, sticky="news", padx=30, pady=30)

        self.v = StringVar() #variable that the input will be stored to temporarily
        self.v.set("Pick a question type")
        self.dropdown = tk.OptionMenu(self, self.v, "Pick a question type", "Addition", "Subtraction", "Multiplication", "Division")
        self.dropdown.grid(row=1, column=1, sticky="news", padx=15, pady=30)

        self.dropdown.config(font=other_font, width=25, background="#F3A89C")


        self.question_no_label = ttk.Label(self, text="# of questions", font=other_font, background="#FDF6E7").grid(row=2, column=0, sticky="news", padx=30, pady=30)

        self.w = IntVar() #variable that the input will be stored to temporarily
        self.question_no = ttk.Entry(self, textvariable=self.w, font=("Comic Sans MS", 10))
        self.question_no.grid(row=2, column=1, sticky="news", padx=15, pady=30)

        #command for go_button
        #decides how to show Frame_Questions
        def go():
            global question_type
            global no_questions
            question_type = self.v.get()
            no_questions = int(self.w.get())
            if not (question_type == "Pick a question type" or no_questions == 0):
                self.grid_forget()
                self.controller.init_frame_questions()
                self.controller.show_frame(Frame_Questions)

        self.go_button = tk.Button(self, text="Go!", font=other_font, background="#F3A89C", foreground="white")
        self.go_button.grid(row=3, column=1, sticky="news", padx=10, pady=30)
        self.go_button.config(command=go)

        self.grid_forget()

#leaderboard frame
class Frame_Leaderboard(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg="#EADB18")
        self.controller = controller

        #creates frame components
        self.photo = PhotoImage(file="background.png")
        self.bg_panel = ttk.Label(self, image=self.photo)
        self.bg_panel.place(x=0, y=0) 

        self.leaderboard_title = ttk.Label(self, text="Leaderboard", font=title_font, background="#ffffe0") 
        self.leaderboard_title.grid(row=0, column=1, sticky="news", padx=250, pady=20)
        self.grid_forget()

        self.lb_label = ttk.Label(self, text=lb.print_leaderboard(username), font=other_font, background="#F6C5B6")
        self.lb_label.grid(row=1, column=1, sticky=NSEW, padx=250, pady=80)

#frame where the questions will be displayed
class Frame_Questions(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg="#EADB18")
        self.controller = controller

        self.addition_word_problems = ["There are ### ducks in a pond.\nThen, *** more ducks join them.\nHow many ducks are now in the pond?",
                          "John eats ### apples.\nThen, he gets hungry and eats *** more.\nHow many apples did John eat?"]

        self.subtraction_word_problems = ["Sarah buys ### pencils.\nThen she loses *** of them.\nHow many pencils does Sarah have now?",
                             "There were ### birds on a fencepost.\nThen, *** of them flew away.\nHow many birds are now on the fencepost?"]

        self.multiplication_word_problems = ["Tim has ### boxes of *** chocolates each.\nHow many chocolates does Tim have?",
                                "There are ### blackberry bushes with *** blackberries each.\nHow many blackberries are there total?"]

        self.division_word_problems = ["Susan has ### slices of pizza to share among *** people,\nnot including herself.\nHow many does each person get\nand how many are left over?",
                          "Karen shares ### cupcakes among her *** children.\nHow many does each kid get,\nand how many are left over?"]

        self.total_incorrect = 0
        #creates background image
        self.photo = PhotoImage(file="background.png")
        self.bg_panel = ttk.Label(self, image=self.photo)
        self.bg_panel.place(x=0, y=0) 

        self.num_attempts = 0 #number of attempts on a question, 2 maximum
        self.correct_answer = 0
        self.correct_remainder = 0
        self.counter = 1 #number of questions that have been answered
                
        self.question_type = question_type

        self.word_problem_chance = 0
        self.word_problem = False

        #30% chance the question is a word problem
        self.word_problem_chance = rand.random()
        if self.word_problem_chance <= 0.3:
            self.word_problem = True
        else: 
            self.word_problem = False

        self.question = ""

        #displays the question based on question_type
        if(self.question_type == "Addition"):
            self.question = "#1: " + self.gen_addition()

        elif(self.question_type == "Subtraction"):
            self.question = "#1: " + self.gen_subtraction()

        elif(self.question_type == "Multiplication"):
            self.question = "#1: " + self.gen_multiplication()

        elif(self.question_type == "Division"):

            #adds an entry box for the remainder
            self.remainder_label = ttk.Label(self, text="R", font=other_font, background="#FCE9E7")
            self.remainder_label.grid(row=1, column=2, sticky=W)

            self.remainder = tk.IntVar()
            self.remainder_input = ttk.Entry(self, textvariable=self.remainder, font=text_box_font, width=5)
            self.remainder_input.grid(row=1, column=3, sticky="W", padx=10)

            self.question = "#1: " + self.gen_division()

        #adds frame components
        self.question_label = ttk.Label(self, text=self.question, font=title_font, justify=CENTER, background="#FCE9E7")

        if self.word_problem:
            self.question_label.config(font=("Futura", 14))
        else:
            self.question_label.config(font=title_font)

        #adjusting the position of the question
        self.qpadx = 0
        self.qpady = 0

        if question_type != 'Division':
            self.qpadx = 111
        else:
            self.qpadx = 30

        if self.word_problem:
            self.qpady = 0
        else:
            self.qpady = 20

        self.question_label.grid(row=0, column=1, sticky="news", padx=self.qpadx, pady=self.qpady)


        self.answer_label = ttk.Label(self, text="Answer: ", font=other_font, background="#FCE9E7")
        self.answer_label.grid(row=1, column=0, sticky=W, pady=10)

        self.answer = tk.IntVar() #variable where the answer will temporarily be stored
        self.answer_input = ttk.Entry(self, textvariable=self.answer, font=text_box_font)
        self.answer_input.grid(row=1, column=1, sticky=NSEW, pady=10)

        self.check_answer_button = tk.Button(self, text="Check Answer", font=other_font, background="#FDF6E7")
        self.check_answer_button.grid(row=2, column=1, sticky=NSEW, pady=90)
        self.check_answer_button.config(command=self.check_answer)

        self.next_question_button = tk.Button(self, text="Next Question", font=other_font, background="#FDF6E7")
        self.next_question_button.grid(row=2, column=1, sticky=NSEW, pady=90)
        self.next_question_button.config(command=self.next_question)
        self.next_question_button.grid_forget()

        self.reaction_label = ttk.Label(self, text="", font=("Comic Sans MS", 14), background="#F9E3DF", justify=CENTER)
        self.reaction_label.grid(row=3, column=1, sticky=S)
        self.reaction_label.grid_forget()
        self.grid_forget()

    #creates questions and stores the correct answer(s) to a variable
    def gen_addition(self):
        num1 = rand.randint(1, 99)
        num2 = rand.randint(1, 99)
        self.correct_answer = num1 + num2
        if self.word_problem:
            question = rand.choice(self.addition_word_problems)
            question = question.replace("###", str(num1))
            question = question.replace("***", str(num2))
            return question
        else:    
            return f"What is {num1} + {num2}?"

    def gen_subtraction(self):
        num1 = rand.randint(1, 99)
        num2 = rand.randint(1, 99)
        while num2 >= num1:
            num2 = rand.randint(1, 9)
        self.correct_answer = num1 - num2
        if self.word_problem:
            question = rand.choice(self.subtraction_word_problems)
            question = question.replace("###", str(num1))
            question = question.replace("***", str(num2))
            return question
        else:
            return f"What is {num1} - {num2}?"

    def gen_multiplication(self):
        num1 = rand.randint(1, 99)
        num2 = rand.randint(1, 9)
        self.correct_answer = num1 * num2
        if self.word_problem:
            question = rand.choice(self.multiplication_word_problems)
            question = question.replace("###", str(num1))
            question = question.replace("***", str(num2))
            return question
        else:
            return f"What is {num1} x {num2}?"
    
    def gen_division(self):
        num1 = rand.randint(1, 99)
        num2 = rand.randint(1, 9)
        while num2 >= num1:
            num2 = rand.randint(1, 9)
        self.correct_answer = math.floor(num1 / num2)
        self.correct_remainder = num1 % num2
        if self.word_problem:
            num1 = rand.randint(2, 99)
            num2 = rand.randint(2, 9)
            while num2 >= num1:
                num2 = rand.randint(2, 9)
            self.correct_answer = math.floor(num1 / num2)
            self.correct_remainder = num1 % num2
            question = rand.choice(self.division_word_problems)
            question = question.replace("###", str(num1))
            question = question.replace("***", str(num2))
            return question
        else:
            return f"What is {num1} \u00F7 {num2}?"
    
    #command for check_answer_button
    def check_answer(self):
        global correct_answers
        global score
        global question_type

        user_answer = int(self.answer.get())
        if question_type == "Division":
            user_remainder = int(self.remainder.get())

        self.num_attempts += 1

        if self.total_incorrect <= math.floor(no_questions * 1.5):
            if question_type == "Division":

                #if it has been two attempts and still hasn't gotten the right answer
                if self.num_attempts >= 2 and (user_answer != self.correct_answer or user_remainder != self.correct_remainder):
                    self.reaction_label.config(text=f"Sorry, that's incorrect\nThe correct answer is {self.correct_answer}R{self.correct_remainder}.")
                    self.reaction_label.grid(row=3, column=1, sticky=NSEW, pady=20, padx=80)
                    self.check_answer_button.grid_forget()
                    self.next_question_button.grid(row=2, column=1, sticky=W, pady=90, padx=20)
                    self.total_incorrect += 1

                #if it has been one attempt and wrong answer
                elif user_answer != self.correct_answer or user_remainder != self.correct_remainder:
                    self.reaction_label.config(text="Sorry, incorrect")
                    self.reaction_label.grid(row=3, column=1, sticky=W, padx=50, pady=45)
                    self.total_incorrect += 1

                #correct answer
                elif user_answer == self.correct_answer and user_remainder == self.correct_remainder:
                    correct_answers += 1
                    self.reaction_label.config(text="Good job!")
                    self.reaction_label.grid(row=3, column=1, sticky=W, padx=80, pady=50)
                    self.check_answer_button.grid_forget()
                    self.next_question_button.grid(row=2, column=1, sticky=S, pady=90, padx=20)

                    #score is based on number of attempts
                    if self.num_attempts == 1:
                        score += 10
                    else: 
                        score += 5

            else: #same but for when the question_type is not Division
                if self.num_attempts >= 2 and user_answer != self.correct_answer:
                    self.reaction_label.config(text=f"Sorry, that's incorrect.\nThe correct answer is {self.correct_answer}.")
                    self.reaction_label.grid(row=3, column=1, sticky=NSEW, padx=50)
                    self.check_answer_button.grid_forget()
                    self.next_question_button.grid(row=2, column=1, sticky=W, pady=90, padx=20)
                    self.total_incorrect += 1

                elif user_answer != self.correct_answer:
                    self.reaction_label.config(text="Sorry, incorrect")
                    self.reaction_label.grid(row=3, column=1, sticky=W, padx=50, pady=45)
                    self.total_incorrect += 1

                elif user_answer == self.correct_answer:
                    correct_answers += 1
                    self.reaction_label.config(text="Good job!")
                    self.reaction_label.grid(row=3, column=1, sticky=W, padx=30, pady=50)
                    self.check_answer_button.grid_forget()
                    self.next_question_button.grid(row=2, column=1, sticky=S, pady=90, padx=20)
                    if self.num_attempts == 1:
                        score += 10
                    else: 
                        score += 5
        else:
            lb.write_leaderboard(f"{username} {score}")
            self.question_label.config(text=f"{username}, your score is {score}!\nYou got {correct_answers} question(s) right out of {no_questions}", font=("Comic Sans MS", 24))
            self.answer_label.grid_forget()
            self.answer_input.grid_forget()
            self.reaction_label.grid_forget()
            self.next_question_button.grid_forget()
            self.check_answer_button.grid_forget()
            if question_type == "Division":
                self.remainder_label.grid_forget()
                self.remainder_input.grid_forget()

            leaderboard_button = tk.Button(self, text="Leaderboard", background="#EB5445", font=other_font)
            leaderboard_button.grid(row=1, column=1, sticky="news", pady=150)

            def show_frame_leaderboard():
                self.controller.init_frame_leaderboard()
                self.controller.show_frame(Frame_Leaderboard)

            leaderboard_button.config(command=show_frame_leaderboard)

    #command for the next_question_button
    def next_question(self):
        self.num_attempts = 0
        self.counter += 1

        self.word_problem_chance = rand.random()
        if self.word_problem_chance <= 0.3:
            self.word_problem = True
        else: 
            self.word_problem = False

        if(self.counter <= no_questions and self.total_incorrect <= math.floor(no_questions * 1.5)):
            if self.word_problem:
                self.question_label.config(font=("Futura", 14))
                self.qpady = 0
            else:
                self.question_label.config(font=title_font)
                self.qpady=20

            if question_type == "Addition":
                self.question = f"#{self.counter}: {self.gen_addition()}"
            elif question_type == "Subtraction":
                self.question = f"#{self.counter}: {self.gen_subtraction()}"
            elif question_type == "Multiplication":
                self.question = f"#{self.counter}: {self.gen_multiplication()}"
            elif question_type == "Division":
                self.question = f"#{self.counter}: {self.gen_division()}"
                self.remainder_input.delete(first=0, last=END)
                
            
            
            #resets the screen
            self.reaction_label.grid_forget()
            self.check_answer_button.grid(row=2, column=1, sticky=S, pady=90)
            self.question_label.config(text=self.question)
            self.answer_input.delete(first=0, last=END)
            self.next_question_button.grid_forget()

        else: #when all of the questions have been answered

            #clears the screen and displays results and leaderboard_button
            lb.write_leaderboard(f"{username} {score}")
            self.question_label.config(text=f"{username}, your score is {score}!\nYou got {correct_answers} question(s) right out of {no_questions}", font=("Comic Sans MS", 24))
            self.answer_label.grid_forget()
            self.answer_input.grid_forget()
            self.reaction_label.grid_forget()
            self.next_question_button.grid_forget()
            self.check_answer_button.grid_forget()
            if question_type == "Division":
                self.remainder_label.grid_forget()
                self.remainder_input.grid_forget()

            leaderboard_button = tk.Button(self, text="Leaderboard", background="#EB5445", font=other_font)
            leaderboard_button.grid(row=1, column=1, sticky="news", pady=150)

            def show_frame_leaderboard():
                self.controller.init_frame_leaderboard()
                self.controller.show_frame(Frame_Leaderboard)

            leaderboard_button.config(command=show_frame_leaderboard)
