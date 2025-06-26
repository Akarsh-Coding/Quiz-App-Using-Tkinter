import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
from time import strftime
import json

class QuizQuestions:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Time")
        self.root.state('zoomed')  # Maximize window
        self.root.resizable(False, False)  # Disable resizing

        # Title label
        self.lbl_title = tk.Label(self.root,
            text="Quiz Time",
            font=("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"),
            bg="#1C1C1C", fg="#00FF00", anchor="center")
        self.lbl_title.place(x=0, rely=0.12, height=60, width=self.root.winfo_screenwidth())

        # Time label
        self.time_lbl = tk.Label(self.lbl_title,
            font=("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"),
            bg="#1C1C1C", fg="#00FF00")
        self.time_lbl.place(relx=0.925, height=55)

        # Function to update time every second
        def Time():
            string = strftime('%I:%M:%S\n%p')
            self.time_lbl.config(text=string)
            self.time_lbl.after(1000, Time)
        Time()

        # Date label
        self.date_lbl = tk.Label(self.lbl_title,
            font=("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"),
            bg="#1C1C1C", fg="#00FF00")
        self.date_lbl.place(relx=0.005, height=55)

        # Function to update date every minute
        def date():
            string = strftime('%A\n%d-%m-%Y')
            self.date_lbl.config(text=string)
            self.date_lbl.after(60000, date)
        date()

        # Frame for displaying questions
        self.Q_frame = tk.LabelFrame(self.root, bd=3, bg="#1C1C1C", fg="#00FFFF",
            relief="ridge", text="?", font=("Times New Roman", 90, "bold"), labelanchor="w")
        self.Q_frame.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.3, anchor='center')

        # Label inside the question frame
        self.Q_label = tk.Label(self.Q_frame, bg="#1c1c1c", fg="#FFFFFF", bd=0,
            text="Press the 'Next' button to begin the quiz.", justify="center",
            font=("Courier New", 35, "bold"))
        self.Q_frame.bind("<Configure>", lambda event: self.Q_label.config(wraplength=event.width - 100))
        self.Q_label.place(relheight=0.975, relwidth=0.975, relx=0.5, rely=0.5, anchor="center")

        # Style for radio buttons
        style = ttk.Style()
        style.configure("Quiz.TRadiobutton", background="#1c1c1c", foreground="#00FFFF",
                        font=("Courier New", 14, "bold"), indicatorcolor="#00FF66", padding=10)
        style.map("Quiz.TRadiobutton",
                  background=[("active", "#1f1f1f")],
                  foreground=[("selected", "#00FF66"), ("active", "#FFFFFF")])

        # Initialize radio button and variables
        self.selected = tk.StringVar()
        self.options = []
        self.users_ans = {}

        self.btn_1 = ttk.Radiobutton(self.root, text="Option 1", value="1", variable=self.selected, style="Quiz.TRadiobutton")
        self.btn_1.place(relx=0.5, rely=0.65, anchor="center")

        self.btn_2 = ttk.Radiobutton(self.root, text="Option 2", value="2", variable=self.selected, style="Quiz.TRadiobutton")
        self.btn_2.place(relx=0.5, rely=0.725, anchor="center")

        self.btn_3 = ttk.Radiobutton(self.root, text="Option 3", value="3", variable=self.selected, style="Quiz.TRadiobutton")
        self.btn_3.place(relx=0.5, rely=0.8, anchor="center")

        self.btn_4 = ttk.Radiobutton(self.root, text="Option 4", value="4", variable=self.selected, style="Quiz.TRadiobutton")
        self.btn_4.place(relx=0.5, rely=0.875, anchor="center")

        # Previous and Next buttons
        self.pre_btn = tk.Button(self.root, text="< Previous", bd=0, bg="#2d2d2d", fg="#00CCFF", state="disabled",
                                 font=("Courier New", 14, "bold"), command=self.pre_questions)
        self.pre_btn.place(relx=0.25, rely=0.9, anchor="center")

        self.nxt_btn = tk.Button(self.root, text="Next >", bd=0, bg="#2D2D2D", fg="#00CCFF",
                                 font=("Courier New", 14, "bold"), command=self.nxt_questions)
        self.nxt_btn.place(relx=0.75, rely=0.9, anchor="center")

        self.current_index = 0  # Track current question
        self.score = 0          # Final score
        self.load_questions()  # Load questions from file

    def load_questions(self):
        with open("Questions.json", "r") as file:
            self.data = json.load(file)
        return self.data

    # Load next question
    def nxt_questions(self):
        data = self.data
        ans = self.selected.get()

        if self.current_index < len(data):
            self.users_ans[self.current_index] = f"{ans}"
            self.selected.set("")  # Reset selection

        if self.current_index < len(data):
            new_data = data[self.current_index]
            self.Q_label.config(text=f"Question {str(new_data['ID'])}:\n{new_data['Q']}", font=("Courier New", 20, "bold"))

            self.options.clear()
            option_data = new_data["choices"]
            for i in option_data:
                self.options.append(i)
            self.btn_1.config(text=f"{self.options[0]}", value=f"{self.options[0]}")
            self.btn_2.config(text=f"{self.options[1]}", value=f"{self.options[1]}")
            self.btn_3.config(text=f"{self.options[2]}", value=f"{self.options[2]}")
            self.btn_4.config(text=f"{self.options[3]}", value=f"{self.options[3]}")

            self.current_index += 1

            if self.current_index > 1:
                self.pre_btn.config(state="normal")

        elif self.current_index == len(data):
            # End of quiz: calculate score
            for i in range(len(self.users_ans)):
                if data[i]["A"] == self.users_ans.get(i + 1):
                    self.score += 1

            self.btn_1.place_forget()
            self.btn_2.place_forget()
            self.btn_3.place_forget()
            self.btn_4.place_forget()
            self.Q_label.config(text=f"\U0001F389 Quiz Completed!\n\U0001F3AF Your Final Score: {(self.score / len(self.users_ans)) * 100:.2f}%",
                                font=("Courier New", 35, "bold"))
            self.pre_btn.place_forget()
            self.nxt_btn.config(text="Response Sheet", font=("Courier New", 20, "bold"))
            self.nxt_btn.place(relx=0.5, rely=0.9, anchor="center")

            self.current_index += 1

        else:
            # Show detailed answer sheet
            self.Q_frame.config(text="Response Sheet", labelanchor="n", font=("Courier New", 25, "bold"))
            self.Q_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')
            self.check_ans(data)
            self.nxt_btn.place_forget()

    # Function to display detailed response sheet
    def check_ans(self, data):
        self.score = 0
        result_text = ""

        for i in range(len(self.users_ans)):
            q_id = data[i]["ID"]
            question = data[i]["Q"]
            correct_ans = data[i]["A"]
            user_ans = self.users_ans.get(i + 1)

            if correct_ans == user_ans:
                self.score += 1

            result_text += f"\nQ{q_id}: {question}\nYour Answer: {user_ans}\t\tCorrect Answer: {correct_ans}\n"

        self.Q_label.config(font=("Courier New", 15, "bold"), justify="left", text=result_text)

    # Function to load previous question
    def pre_questions(self):
        data = self.data
        if self.current_index >= 1:
            self.current_index -= 1
            new_data = data[self.current_index - 1]
            self.Q_label.config(text=f"Question {str(new_data['ID'])}:\n{new_data['Q']}", font=("Courier New", 20, "bold"))

            self.options.clear()
            option_data = new_data["choices"]
            for i in option_data:
                self.options.append(i)
            self.btn_1.config(text=f"{self.options[0]}")
            self.btn_2.config(text=f"{self.options[1]}")
            self.btn_3.config(text=f"{self.options[2]}")
            self.btn_4.config(text=f"{self.options[3]}")

        if self.current_index == 1:
            self.pre_btn.config(state="disabled")
        else:
            self.pre_btn.config(state="normal")

# Main app window
if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#1C1C1C")
    app = QuizQuestions(root)
    root.mainloop()
