from tkinter import *
from tkinter import messagebox
from dev.app.app import generate_password
from dev.app.constants import *


def gui():
    window = Tk()
    window.title("PASSWORD-GENERATOR")
    icon = PhotoImage(file='./app/img/photo.png')
    window.iconphoto(True, icon)
    window.configure(bg=BG_COLOR)
    window.attributes('-fullscreen', True)

    def exit_program():
        new_window.destroy()
        window.destroy()

    def open_new_window():
        window.withdraw()
        global new_window
        global length
        new_window = Toplevel()
        new_window.configure(bg=BG_COLOR)
        new_window.attributes('-fullscreen', True)

        def getLength() -> int:
            length = entry.get()
            if len(length) == 0:
                messagebox.showerror(title="Error happened",
                                     message="Firstly you have to give the length!")
            elif not length.isdigit():
                messagebox.showerror(title="Error happened",
                                     message="Incorrect data type!")
            elif int(length) < 4:
                messagebox.showerror(title="Error happened",
                                     message="Incorrect length of password!")
            else:
                return int(length)

        def generate_fun():
            if x.get() == 0:
                listbox.insert(listbox.size(), generate_password("Easy", getLength()))
            elif x.get() == 1:
                listbox.insert(listbox.size(), generate_password("Medium", getLength()))
            elif x.get() == 2:
                listbox.insert(listbox.size(), generate_password("Strong", getLength()))

        def delete():
            for index in reversed(listbox.curselection()):
                listbox.delete(index)

        def save_to_file():
            for index in reversed(listbox.curselection()):
                with open("passwords.txt", "a") as f:
                    f.write(listbox.get(index) + "\n")

        myLabel3 = Label(new_window,
                         text="\nGive the length of password (min = 4): ",
                         font=(FONT, 20),
                         fg=NEW_WINDOW_COLOR,
                         bg=BG_COLOR)

        entry = Entry(new_window, width=40, borderwidth=4, font=(FONT, 12, "bold"))

        myLabel4 = Label(new_window,
                         text="\nChose the level of security to your password: ",
                         font=(FONT, 20),
                         fg=NEW_WINDOW_COLOR,
                         bg=BG_COLOR)

        check_frame = Frame(new_window, pady=10)
        check_frame.configure(bg=BG_COLOR)

        list_frame = Frame(new_window, pady=10)
        list_frame.configure(bg=BG_COLOR)

        myLabel5 = Label(new_window,
                         text="\nEasy-additional big letters\n"
                              "Medium-additional big letters & numbers\n"
                              "Strong-additional big letters & numbers & special characters",
                         font=(FONT, 14),
                         fg=NEW_WINDOW_COLOR,
                         bg=BG_COLOR)
        options = ["Easy", "Medium", "Strong"]
        x = IntVar()
        for index in range(len(options)):
            radio_button = Radiobutton(check_frame,
                                       text=options[index],
                                       bg=BUTTON_COLOR,
                                       fg=NEW_WINDOW_COLOR,
                                       font=(FONT, 12, "bold"),
                                       activebackground=BUTTON_COLOR,
                                       activeforeground=NEW_WINDOW_COLOR,
                                       variable=x,
                                       value=index,
                                       bd=3,
                                       padx=12,
                                       pady=8,
                                       relief=GROOVE)
            radio_button.pack(side=LEFT, padx=5)

        generate_button = Button(new_window,
                                 text="GENERATE",
                                 padx=40,
                                 pady=15,
                                 font=(FONT, 12, "bold"),
                                 bg=NEW_WINDOW_COLOR,
                                 fg=BUTTON_COLOR,
                                 activebackground=BUTTON_COLOR,
                                 activeforeground=NEW_WINDOW_COLOR,
                                 bd=3,
                                 relief=GROOVE,
                                 command=generate_fun)

        listbox = Listbox(new_window, width=40, font=(FONT, 12, "bold"), bd=3)
        delete_button = Button(list_frame,
                               text="DELETE",
                               command=delete,
                               padx=10,
                               pady=10,
                               font=(FONT, 12, "bold"),
                               bg=BUTTON_COLOR,
                               fg=NEW_WINDOW_COLOR,
                               activebackground=NEW_WINDOW_COLOR,
                               activeforeground=BUTTON_COLOR,
                               bd=3,
                               relief=GROOVE)
        save_button = Button(list_frame,
                             text="SAVE",
                             command=save_to_file,
                             padx=10,
                             pady=10,
                             font=(FONT, 12, "bold"),
                             bg=BUTTON_COLOR,
                             fg=NEW_WINDOW_COLOR,
                             activebackground=NEW_WINDOW_COLOR,
                             activeforeground=BUTTON_COLOR,
                             bd=3,
                             relief=GROOVE)

        exit_button = Button(new_window,
                             text="EXIT",
                             command=exit_program,
                             padx=40,
                             pady=10,
                             font=(FONT, 12, "bold"),
                             bg=NEW_WINDOW_COLOR,
                             fg=BUTTON_COLOR,
                             activebackground=BUTTON_COLOR,
                             activeforeground=NEW_WINDOW_COLOR,
                             bd=3,
                             relief=GROOVE)

        myLabel3.pack(anchor=CENTER, pady=10)
        entry.pack(anchor=CENTER)
        myLabel4.pack()
        myLabel5.pack()
        check_frame.pack(pady=20)
        generate_button.pack(pady=15)
        listbox.pack(pady=10)
        delete_button.pack(side=LEFT, padx=10)
        save_button.pack(side=LEFT)
        list_frame.pack()
        exit_button.pack(side=BOTTOM, anchor=CENTER)

    button_frame = Frame(window, padx=10, pady=10)
    button_frame.configure(bg=BG_COLOR)

    myLabel1 = Label(window,
                     text="WELCOME IN PASSWORD GENERATOR!",
                     font=(FONT, 25),
                     fg=TEXT_COLOR,
                     bg=BG_COLOR)
    myLabel2 = Label(window,
                     text="\n\nPress \"START\" to generate a password or \"QUITE\" to exit\n",
                     font=(FONT, 18),
                     fg=TEXT_COLOR,
                     bg=BG_COLOR)
    startButton = Button(button_frame,
                         text="START",
                         command=open_new_window,
                         padx=40, pady=15,
                         font=(FONT, 12, "bold"),
                         fg=TEXT_COLOR,
                         bg=BUTTON_COLOR,
                         activebackground=TEXT_COLOR,
                         activeforeground=BUTTON_COLOR,
                         bd=3,
                         relief=GROOVE)
    quiteButton = Button(button_frame,
                         text="QUITE",
                         command=window.quit,
                         padx=40,
                         pady=15,
                         font=(FONT, 12, "bold"),
                         bg=TEXT_COLOR,
                         fg=BUTTON_COLOR,
                         activebackground=BUTTON_COLOR,
                         activeforeground=TEXT_COLOR,
                         bd=3,
                         relief=GROOVE)

    myLabel1.pack(pady=150)
    myLabel2.pack()
    startButton.pack(side=LEFT, padx=10)
    quiteButton.pack(side=RIGHT, padx=10)
    button_frame.pack()
    window.mainloop()
