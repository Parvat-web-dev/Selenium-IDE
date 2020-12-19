#I am trying to create a Selenium IDE
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

                                                                                                                
'''
Blue Print:
    Keys:
        '|any|' represents the string got from user.
        '!any!' represents the variable declared before the use!
    -A class that contains all the function.
        __init__(self, browser, file_name):
                -it gets the browser's name (chrome or firefox),
                the appends the eval(text:
                                    from selenium import webdriver
                                    from selenium.webdriver.common.keys import Keys
                                    browser = webdriver.|self.browser|()
                                    )
                at the end of the |file_name|.py file.
                
        go_to(self, link):
                - it gets the link and appends eval(text:
                                                    !browser!.get('|link|')
                                                    )
                at the end of the |file_name|.py file.

        click(self, x_path, element_name):
                -it gets the x_path of an elements an attepts a
                click like this eval(text:
                                        |element_name| = !browser!.find_element_by_xpath('|x_path|')
                                    )
        run(self):
                -it gets the file_name and runs it!
'''



'''
Functions :
    -__init__(browser, file_name)
    -go_to(url)
'''

class Function:

    #The function to get the browser name
    def __init__(self, browser, file_name):
        self.file_name = file_name
        self.browser = (str(browser)).title()
        text_to_append1 = '''from selenium import webdriver

'''
        text_to_append2 = '''from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
        text_to_append4 = 'browser = webdriver.'+self.browser+'()'
        text_to_append3 = '''

'''
        try:
            open_file = open(self.file_name, 'w')
            open_file.write(text_to_append1)
            open_file.close()
            open_file = open(self.file_name, 'a')
            open_file.write(text_to_append2)
            open_file.write(text_to_append3)
            open_file.write(text_to_append4)
            open_file.close()
        except FileNotFoundError:
            print('The file was not found!')
        
    def go_to(self, url):
        text_to_append1 = "browser.get('"+url+"')"
        text_to_append2 = '''

'''
        try:
            open_file = open(self.file_name, 'a')
            open_file.write('''

''')
            open_file.write(text_to_append1)
            open_file.write(text_to_append2)
            open_file.close()
        except FileNotFoundError:
            print('The file was not found!')

    def run(self):
        os.startfile(self.file_name)

    def click(self, x_path, element_name):
        text_to_append1 = '''

'''
        text_to_append2 = ''+str(element_name)+' = '+"browser.find_element_by_xpath('"+str(x_path)+"')"
        text_to_append3 = '''

'''
        text_to_append4 = ''+str(element_name)+'.click()'
        text_to_append5 = '''

'''
        try:
            open_file = open(self.file_name, 'a')
            open_file.write(text_to_append1)
            open_file.write(text_to_append2)
            open_file.write(text_to_append3)
            open_file.write(text_to_append4)
            open_file.write(text_to_append5)
            open_file.close()
        except FileNotFoundError:
            print('The file was not found!')


    def send_text(self, x_path, element_name, text):
        text_to_append1 = '''

'''
        text_to_append2 = ''+element_name+' = '+"browser.find_element_by_xpath('"+str(x_path)+"')"
        text_to_append3 = '''

'''
        text_to_append4 = ''+element_name+'.click()'
        text_to_append5 = '''

'''
        text_to_append6 = ''+element_name+".send_keys('"+str(text)+"')"
        text_to_append7 = '''

'''
        try:
            open_file = open(self.file_name, 'a')
            open_file.write(text_to_append1)
            open_file.write(text_to_append2)
            open_file.write(text_to_append3)
            open_file.write(text_to_append4)
            open_file.write(text_to_append5)
            open_file.write(text_to_append6)
            open_file.write(text_to_append7)
            open_file.close()
        except FileNotFoundError:
            print('The file was not found!')

    

    def hover(self, xpath):
        try:
            text_to_append1 = 'action = ActionChains(browser)'
            text_to_append2 = '''

'''
            text_to_append3 = "action.move_to_element(browser.find_element_by_xpath('"+str(xpath)+"')).perform()"
            text_to_append4 = '''

'''
            open_file = open(self.file_name, 'a')
            open_file.write(text_to_append1)
            open_file.write(text_to_append2)
            open_file.write(text_to_append3)
            open_file.write(text_to_append4)
            open_file.close()
        except :
            print('Some problem occured!')
            

    def send_keys(self, key, element_name, x_path):
        text_to_append1 = '''

'''
        text_to_append2 = ''+element_name+' = '+"browser.find_element_by_xpath('"+str(x_path)+"')"
        text_to_append3 = '''

'''
        text_to_append5 = '''

'''
        text_to_append6 = ''+element_name+".send_keys(Keys."+key+")"
        text_to_append7 = '''

'''
        try:
            open_file = open(self.file_name, 'a')
            open_file.write(text_to_append1)
            open_file.write(text_to_append2)
            open_file.write(text_to_append3)
            open_file.write(text_to_append5)
            open_file.write(text_to_append6)
            open_file.write(text_to_append7)
            open_file.close()
        except FileNotFoundError:
            print('An Error occured!')






