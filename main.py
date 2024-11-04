from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK = 25*60
SHORT_BREAK = 5*60
LONG_BREAK = 20*60
reps = 1

# ---------------------------- PROGRAM ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

label = Label(window, text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

checkmark = Label(window, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))

timer_event = None


def timer_mechanism(id_, seconds):
    global timer_event
    global reps
    label.config(text="WORK", fg=RED)
    minus, secs = divmod(seconds, 60)
    timer = "{:02d}:{:02d}".format(minus, secs)
    canvas.itemconfig(id_, text=timer)
    if seconds > 0:
        timer_event = window.after(1000, timer_mechanism, id_, seconds - 1)
    else:
        checkmark["text"] += " ✔"
        checkmark.grid(column=1, row=2)
        if reps % 4 == 0:
            timer_break(text_id, LONG_BREAK)
        else:
            timer_break(text_id, SHORT_BREAK)


def timer_break(id_, seconds):
    global timer_event, reps
    label.config(text="BREAK", fg=GREEN)
    minus, secs = divmod(seconds, 60)
    timer = "{:02d}:{:02d}".format(minus, secs)
    canvas.itemconfig(id_, text=timer)
    if seconds > 0:
        timer_event = window.after(1000, timer_break, id_, seconds - 1)
    else:
        reps += 1
        timer_mechanism(text_id, WORK)


def start_timer():
    timer_mechanism(text_id, WORK)


def stop_timer():
    global timer_event
    window.after_cancel(timer_event)
    canvas.itemconfig(text_id, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")


button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

button2 = Button(text="Stop", command=stop_timer)
button2.grid(column=2, row=2)

window.mainloop()
