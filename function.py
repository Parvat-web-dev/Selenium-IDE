from SeleniumModule import *
from tkinter import *
import os
import random as r
#The IDE
element_num = 0
element = 'element_'

#this ide will be imported in the 'main.py'
def IDE(url, browser, file_name):
    a = Function(browser, file_name)
    a.go_to(url)
    #The main window:
    ide_window = Tk()
    ide_window.geometry('500x500')
    ide_window.config(bg = 'white')
    ide_window.focus_force()
    ide_window.resizable(width = False, height = False)

    #The xpath menu
    xpath_label = Label(ide_window, text = 'X-path : ', fg = 'black', bg = 'white')
    xpath_label.config(font = 'Courier 20')
    xpath_label.place(x = 10, y = 100)
    xpath_ipt = Entry(ide_window)
    xpath_ipt.config(font = 'Courier 20', bg = 'skyblue', fg = 'darkblue')
    xpath_ipt.place(x = 140, y = 100)

    #The command options:
    options = ['click', 'send_text', 'hover', 'send_key']
    display_options = StringVar(ide_window)
    display_options.set('click')
    option_bar = OptionMenu(ide_window, display_options, *options)
    option_bar.config(font = 'Arial 20')
    option_bar.place(x = 200, y = 150)

    #the text box:
    text_label = Label(ide_window, text = 'Text : ', fg = 'black', bg = 'white')
    text_label.config(font='Courier 20')
    text_label.place(x = 10, y = 230)

    text_ipt = Entry(ide_window, fg = 'white', bg = 'black')
    text_ipt.config(font = 'Courier 20')
    text_ipt.place(x = 120, y = 230)

    #The send text option:
    KEYS = ['ADD',
            'ALT',
            'ARROW_DOWN',
            'ARROW_LEFT',
            'ARROW_RIGHT',
            'ARROW_UP',
            'BACKSPACE',
            'BACK_SPACE',
            'CANCEL',
            'CLEAR',
            'COMMAND',
            'CONTROL',
            'DECIMAL',
            'DIVIDE',
            'DELETE',
            'DOWN',
            'END',
            'ENTER',
            'EQULAS',
            'ESCAPE',
            'F1',
            'F10',
            'F11',
            'F2',
            'F3',
            'F4',
            'F5',
            'F6',
            'F7',
            'F8',
            'F9',
            'HELP',
            'HOME',
            'INSERT',
            'LEFT',
            'LEFT_ALT',
            'LEFT_CONTROL',
            'LEFT_SHIFT',
            'META',
            'MULTIPLY',
            'NULL',
            'NUMPAD0',
            'NUMPAD1',
            'NUMPAD2',
            'NUMPAD3',
            'NUMPAD4',
            'NUMPAD5',
            'NUMPAD6',
            'NUMPAD7',
            'NUMPAD8',
            'NUMPAD9',
            'PAGE_DOWN',
            'PAGE_UP',
            'PAUSE',
            'RETURN',
            'SEMICOLON',
            'SEPERATOR',
            'SHIFT',
            'SPACE',
            'SUBTRACT',
            'TAB',
            'UP'
            ]
    key = StringVar()
    key.set(KEYS[17])
    keys_display = OptionMenu(ide_window, key, *KEYS)
    keys_display.config(font = 'Courier 20')
    keys_display.place(x = 350, y = 150)
    
    element_num = 0
    element = 'element_'
    #The Add Command:
    def Add():
        element_name = element + str(r.randint(0, 10000000))
        text = text_ipt.get()
        selected_key = key.get()
        xpath = xpath_ipt.get()
        option = display_options.get()
        if option == options[0]:#click
            a.click(xpath, element_name)
        if option == options[1]:#send_text
            a.send_text(xpath, element_name, text)
        if option == options[2]:#hover
            a.hover(xpath)
        if option == options[3]:#send_key
            a.send_keys(selected_key, element_name, xpath)
    add_btn = Button(ide_window, text = 'Add', fg = 'lightgreen', bg = 'darkblue', command = Add)
    add_btn.config(font = 'Courier 20')
    add_btn.place(x = 10, y = 150)
    File = file_name
    #The run button:
    def run():
        os.startfile(File)

    run_btn = Button(ide_window, text=' RUN ', fg = 'white', bg = 'green', command = run)
    run_btn.config(font='Corier 20')
    run_btn.place(x = 200, y = 300)

    def Exit():
        ide_window.destroy()

    exit_btn = Button(ide_window, text = 'Quit', bg = 'red', fg = 'white', command = Exit)
    exit_btn.config(font = 'Courier 10')
    exit_btn.place(x = 400, y = 450)
    
    ide_window.mainloop()
#/html/body/div/header/div/nav/ul/li[2]/a
#/html/body/div/header/div/nav/ul/li[2]/ul/li[3]/a
