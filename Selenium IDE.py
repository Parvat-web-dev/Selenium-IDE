from SeleniumModule import *
from tkinter import *
import webbrowser
import function as IDE

'''
Blue Print :

    -A process tree:
                                Main Window
                                     |
              _______________________|________________________
             |             ^                                  |
             |             |                                  |
            Help------------                                 IDE

    -Main Window:
        -A window that asks a base URL to launch the browser
        -A option manu to get the default BROWSER
        -A window with help_menu and start_ide button
        
    -HELP:
        -A window with a back button!
        -This window teaches how to use this IDE!

    -IDE:
        -A input field for getting the x-path,
        -A option menu to get the command like click or send_keys
        -A show button to show the file where the functions are written
        -A button to append the command with the xpath
        -A function to RUN the commands added till now
'''



##### -------------The help Menu--------------- #####
def help_menu():
    #Creating the help window and its configuration:
    help_window = Tk()
    help_window.geometry('680x500')
    help_window.resizable(width = False, height = False)
    help_window.title('HELP -- Selenium IDE')
    help_window.config(bg = 'black')
    help_window.focus_force()
    #the message to display on the screen:
    help_msg = '''This IDE is simple.
In the main window, you have to input the
base URL that will be opened when you run
the commands. The Option menu in the main
window is two browers as options and asks
you which browser to open when you run as
by default. When you enter the IDE window
you will see a input field which requires
a 'X-path', you can find it by pressing a
combination of Ctrl, Shift, C which is an
inspectory command in the developers menu
then hover you mouse on the element which
you want to know the X-path then click it
of VISIT : '''

    text_display = Label(help_window, text = help_msg, fg = 'white', bg = 'black')
    text_display.config(font = 'Courier 20')
    text_display.place(x = '10', y = '10')

    def visit():
        webbrowser.open('https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath')

    def back():
        help_window.destroy()
    
    button = Button(help_window, text = 'Selenium - X-path', command = visit)
    button.config(fg = 'blue', font = 'Courier 20', bg = 'black')
    button.place(x = 200, y = 435)

    back_btn = Button(help_window, text = '<- Back', command = back)
    back_btn.config(bg = 'red', fg = 'white')
    back_btn.place(x = 0, y = 0)
    
    help_window.mainloop()

#help_menu()

##### ---------------The main window------------------- #####
def mainwindow():
    main_window = Tk()
    main_window.geometry('400x400')
    main_window.config(bg = 'lightgray')
    main_window.title('Main Menu | Selenium IDE')
    main_window.focus_force()

        #The Exit func
    def Exit():
        main_window.destroy()
        

    #The main Text:
    Text = 'Main Menu'
    a = Label(main_window, text = Text, fg = 'black', bg = 'white')
    a.config(font = 'Courier 30')
    a.place(x = 100, y = 10)

    #The browser option
    browsers = ['Chrome', 'Firefox']
    var = StringVar(main_window)
    var.set(browsers[1])

    option = OptionMenu(main_window, var, *browsers)
    option.config(font = 'Courier 16', fg = 'white', bg = 'black')
    option.place(x = 150, y = 60)
        
    #getting the base url.
    url_entry = Entry(main_window)
    url_entry.config(font = 'Courier 18')
    url_entry.place(x = 80, y = 100)

    #The url entry label
    label = Label(main_window, text = 'URL :', fg = 'blue', bg = 'lightgray')
    label.config(font = 'Courier 18')
    label.place(x = 10, y = 100)

    #the file name entry
    file_name = Entry(main_window, fg = 'skyblue', bg = 'darkblue')
    file_name.config(font = 'Courier 18')
    file_name.place(x = 115, y = 150)

    #the file name label
    file_label = Label(main_window,text = 'File Name:', fg = 'black', bg = 'white')
    file_label.config(font = 'Courier 13')
    file_label.place(x = 8, y = 152)
    
    #The start IDE
    def start_ide():
        url = url_entry.get()
        browser = var.get()
        file = file_name.get()
        file = str(file)
        if file.endswith('.py') == False:
            file = file + '.py'
        create_file()
        main_window.destroy()
        element_num = 0
        element = 'element_'
        IDE.IDE(url, browser, file)

    def alert(message):
        prompt = Tk()
        prompt.focus_force()
        prompt.geometry('500x500')
        prompt.resizable(width = False, height = False)
        label = Label(prompt, text = message, fg = 'red', bg = 'white')
        label.config(font = 'Courier 20')
        label.place(x = 10, y = 10)
        def ok():
            prompt.destroy()

        ok_btn = Button(prompt, text=' Ok ', fg = 'black', bg = 'skyblue', command = ok)
        ok_btn.config(font='Courier 16')
        ok_btn.pack(side = BOTTOM)
            
    #Creates a new file.
    def create_file():
        try:
            file = file_name.get()
            if not(str(file).endswith == '.py'):
                file = str(file_name) + '.py'
            f = open(file, 'x')
        except FileExistsError:
            print('File Exists')
            
            
    

    #The proceed to IDE button.
    button = Button(main_window, text = 'Start IDE', fg = 'white', bg = 'green', command = start_ide)
    button.config(font = 'Courier 16')
    button.place(x = 140, y = 200)

    #The help button
    help_btn = Button(main_window, text = 'Help', fg = 'white', bg = 'blue', command = help_menu)
    help_btn.config(font = 'Courier 16')
    help_btn.place(x = 170, y = 250)

    #The exit button:
    quit_btn = Button(main_window, text = 'Exit', fg = 'white', bg = 'red', command = Exit)
    quit_btn.config(font = 'Courier 16')
    quit_btn.place(x = 170, y = 300)
    
    main_window.mainloop()
mainwindow()
##########_______________END OF SCRIPT ___________________##########
