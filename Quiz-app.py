import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkfont
from PIL import Image,ImageTk
from time import strftime
import json

class QuizQuestions:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Time")
        # Make the window start in fullscreen mode
        # self.root.attributes('-fullscreen', True)
        self.root.state('zoomed')  # Maximize window to fit screen
        # Bind the Escape key to exit fullscreen
        # self.root.bind("<Escape>", lambda event: self.toggle_fullscreen())
        self.root.resizable(False,False)



        # # Load and Display background image
        # img_bg = Image.open(r"sample images\Background image.jpg")
        # img_bg = img_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
        #                             Image.Resampling.LANCZOS)
        # self.photo_bg = ImageTk.PhotoImage(img_bg)

        # bg_lbl = tk.Label(self.root, image=self.photo_bg)
        # bg_lbl.place(x=0, y=0, width=self.root.winfo_screenwidth(), 
        #                 height=self.root.winfo_screenheight())  
        # bg_lbl.lower()



        # # Load and Display Logo
        # img_logo = Image.open("sample images/IITP Name&Logo.png")
        # img_logo = img_logo.resize((500, 115), Image.Resampling.LANCZOS)
        # self.photo_logo = ImageTk.PhotoImage(img_logo)

        # l_lbl = tk.Label(self.root, image=self.photo_logo, bg="#D3D3D3")
        # l_lbl.place(x=0, y=5, width=self.root.winfo_screenwidth(), height=115)  # Full width
        # l_lbl.config(anchor="center")   # Make the logo centered



        # title
        lbl_title=tk.Label(self.root, 
                            text="Quiz Time",
                            font= ("Monotype Corsiva", 40, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 40, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" ,anchor="center")
        lbl_title.place(x=0, y=125, height=60, width=self.root.winfo_screenwidth())


        # ========Time==========#
        time_lbl=tk.Label(lbl_title, 
                            
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        time_lbl.place(relx=0.925,height=55)

        def Time():
            string = strftime('%I:%M:%S\n%p')
            time_lbl.config(text=string)
            time_lbl.after(1000, Time)
        Time()


        # ========Date==========#
        date_lbl=tk.Label(lbl_title, 
                            font= ("Monotype Corsiva", 15, "bold") if "Monotype Corsiva" in tkfont.families() else ("Times New Roman", 15, "bold"), 
                            
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )

        date_lbl.place(relx=0.005,height=55,)

        def date():
            string = strftime('%A\n%d-%m-%Y')
            date_lbl.config(text=string)
            # date_lb.after(1000, Time)
            date_lbl.after(60000, date)  # update every minute
        date()

    # --------------------------------------------------------------------------------------
    # Question label frame
        Q_frame=tk.LabelFrame(self.root,bd=3,bg="#1C1C1C",fg="#FFFFFF",relief="ridge",text="?",font=("Times New Roman",90,"bold"),labelanchor="w")
        Q_frame.place(relx=0.5,rely=0.45,relwidth=0.5, relheight=0.3,anchor='center')

    # ----------------------------- Options Radio Buttons ------------------------------- #
        style = ttk.Style()
        # style.theme_use("default")

        # Define custom radio button style
        style.configure("Quiz.TRadiobutton",
                        background="#1c1c1c",
                        foreground="#00FF66",
                        font=("Courier New", 14, "bold"),
                        indicatorcolor="#00FF66",
                        padding=10,
                        
                        focuscolor="")  # remove focus border if needed

        # Change appearance on hover and selection
        style.map("Quiz.TRadiobutton",
                background=[("active", "#1f1f1f")],
                foreground=[("selected", "#FFFFFF"), ("active", "#00FF99")])

        # Variable for selection
        selected = tk.StringVar()

        btn_1=ttk.Radiobutton(self.root,text="OPTION 1",value="1",variable=selected,style="Quiz.TRadiobutton")
        btn_1.place(relx=0.5,rely=0.65,anchor="center")

        btn_2=ttk.Radiobutton(self.root,text="OPTION 2",value="2",variable=selected,style="Quiz.TRadiobutton")
        btn_2.place(relx=0.5,rely=0.725,anchor="center")

        btn_3=ttk.Radiobutton(self.root,text="OPTION 3",value="3",variable=selected,style="Quiz.TRadiobutton")
        btn_3.place(relx=0.5,rely=0.8,anchor="center")

        btn_4=ttk.Radiobutton(self.root,text="OPTION 4",value="4",variable=selected,style="Quiz.TRadiobutton")
        btn_4.place(relx=0.5,rely=0.875,anchor="center")


        # ------------ Previous and next button ----------------- #
        pre_btn = tk.Button(self.root,text="< Previous",bd=0,bg="#2d2d2d",fg="#00CCFF",font=("Courier New", 14, "bold"))
        pre_btn.place(relx=0.25,rely=0.9,anchor="center")

        nxt_btn = tk.Button(self.root,text="Next >",bd=0,bg="#2D2D2D",fg="#00CCFF",font=("Courier New", 14, "bold"))
        nxt_btn.place(relx=0.75,rely=0.9,anchor="center")







if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#1C1C1C")
    app = QuizQuestions(root)
    root.mainloop()
