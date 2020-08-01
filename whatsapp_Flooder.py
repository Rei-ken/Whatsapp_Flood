from selenium import webdriver
import time
import os

def banner():
        print("""

#######################
#                                                     #
#WHATSAPP FLOODER V1.0 #
#                                                     #
#######################
____________________________

-        Coder By Rei-ken            -
____________________________

#######################

""")

def msgbot():
        input("başlamak için enter tuşuna basınız")
        tarayıcı=webdriver.Firefox()
        time.sleep(4)
        tarayıcı.get('https://web.whatsapp.com/')
        input("whatsapp QR kodunu okuttuysanız enter tuşuna basabilirsiniz...")
        name=input("Kullanıcı veya grubun adı :")       
        user=tarayıcı.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        user.click()
        user.send_keys(name)
        time.sleep(1)
        user_pm=tarayıcı.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div')
        user_pm.click()
        word=open("word.txt","r")
        msg=tarayıcı.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg.click()
        for i in word:
                satır=word.readline()
                msg.send_keys(satır)
                
        
banner()
msgbot()

        
        
        

