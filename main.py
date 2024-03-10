from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    Check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_breake_sec = LONG_BREAK_MIN * 60
   
    if reps % 8 ==0:
        count_down(long_breake_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        Check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer",font=(FONT_NAME,50),bg=YELLOW, fg=GREEN)
title_label.grid(row=0,column=1)

#Canvas
canvas =Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="White", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)




Start_Button=Button(text="Start", highlightthickness=0,command=start_timer)
Start_Button.grid(row=2,column=0)

Reset_Button=Button(text="Reset", highlightthickness=0, command=reset_timer)
Reset_Button.grid(row=2,column=2)


Check_mark = Label(font=(FONT_NAME,20),bg=YELLOW, fg=GREEN)
Check_mark.grid(row=3,column=1)








window.mainloop()