# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:21:25 2020

@author: jeevan
"""

def stackoverflow_Login(mail,passw):
    from selenium import webdriver
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
    
    driver.maximize_window()
    
    #mail="" #enter your email_id
    #passw="" #enter password
    
    #key user email
    email=driver.find_element_by_name('email')
    email.send_keys(mail)
    
    #key user password
    password=driver.find_element_by_name('password')
    password.send_keys(passw)
    
    #press login
    login=driver.find_element_by_name('submit-button')
    driver.implicitly_wait(500)
    login.click()

