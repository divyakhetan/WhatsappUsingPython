import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

#list_names = input('Enter the contact names: ')
#list_names = list_names.split(" ")
list_names = list()
n = input('Enter number of contacts')
for i in range(int(n)):
    xyz = input('name: ')
    list_names.append(xyz)
    
print (list_names)
#name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

for names in list_names:
    print(names)
    #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(names))
    #user.click()
    search_field = driver.find_element_by_class_name('jN-F5')
    search_field.send_keys(names + Keys.ENTER)
    try:
        time.sleep(5)
        last_seen = driver.find_element_by_class_name('O90ur').text
        if len(last_seen) > 0:
            print (names + " : " + last_seen)
    except Exception as e:
        pass

    #last_seen = driver.find_element_by_class_name('O90ur').text
    #print (last_seen)

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg + names )
        driver.find_element_by_class_name('_35EW6').click()


