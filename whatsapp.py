import json
import time
import urllib
import base64
import os.path
import requests
import datetime
import BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

######################################################################
# _______________________HTML PARSING_______________________#
try:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    driver.set_window_size(20000, 12000)
    time.sleep(10)# needs to be increased
    html = driver.page_source
    html = BeautifulSoup(html)
except Exception as e:
    print "Exception was caused at HTML Parsing as %s" % (str(e))

##############################################################################
# click using name of chat
try:
    name = raw_input("Enter Chat name correctly:\n")
    number_to_scroll_up = int(raw_input("Enter number for scrolling as per estimated chat messages\n"))
    n = number_to_scroll_up * (0.2)
    name_path = "//span[@title='%s']" % (name)
    # print name_path
    time.sleep(3)
    print "Clicking on Chat"
    click_event = driver.find_element_by_xpath(name_path)
    time.sleep(2)
    click_event.click()
except Exception as e:
    print "Exception was caused at Clicking chat name as %s" % (str(e))

# all_chats = html.findAll('div', attrs={"class":"_1NrpZ"})
# chats = all_chats[0].findAll('span', attrs={"class":"_1wjpf"})

# names = []
# for i in chats:
#   for j in i:
#     names.append(j)

# only_chat_names = []
# for i in names:
#   chats = all_chats[0].findAll('span', attrs={"title":"%s"%i})
#   if chats!=[]:
#     for i in chats:
#       for j in i:
#         only_chat_names.append(j)
#   else:
#     pass

# for i in range(len(only_chat_names)):
#   print only_chat_names[i]
#   name_path = "//span[@title='%s']"%only_chat_names[i]
#   click_event = driver.find_element_by_xpath(name_path)
#   time.sleep(5)
#   try:
#     click_event.click()       #needed
#   except:
#     pass
#   finally:
#     search = driver.find_element_by_class_name("jN-F5")
#     search.send_keys(only_chat_names[i])
#     time.sleep(2)
#     click_event.click()
#     time.sleep(2)
#     cross = driver.find_element_by_xpath("//span[@data-icon='x-alt']")
#     cross.click()

################################################################

time.sleep(2)

time.sleep(2)

##############################################
# Scroll
# print "Scrolling"
# try:
#     move_to = driver.find_element_by_css_selector("body ._2nmDZ")

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(4)

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(4)

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(n)

#     for i in range(20):
#         move_to.send_keys(Keys.HOME)
# except Exception as e:
#     print "Exception was caused at Scrolling as %s" % (str(e))
time.sleep(3)
start_msg = []
while start_msg==[]:
    print "in while"
    html = driver.page_source
    html = BeautifulSoup(html)
    move_to = driver.find_element_by_css_selector("body ._2nmDZ")
    start_msg = html.findAll('div', attrs={"class":"_3_7SH _14b5J Zq3Mc tail"})
    print start_msg
    # text = []
    # if start_msg != []:
    #   for i in start_msg:
    #     for j in i:
    #       for k in j:
    #         for l in k:
    #           for m in l:
    #             print m
    #             text.append(m)
    #add condition for m if needed(text at top of the chat)
    if start_msg==[]:
      for i in range(10):
        move_to.send_keys(Keys.HOME)
        time.sleep(0.5)
    else:
      print "exit"




###########################################################################################
# _______________________TO GET HTML ELEMENTS FROM NEWLY LOADED PAGE_______________________#
try:
    time.sleep(2)
    html1 = driver.page_source
    html = BeautifulSoup(html1)
    # soup = BeautifulSoup(html, 'html.parser')
except Exception as e:
    print "Exception was caused at Parsing newly loaded HTML elements as %s" % (str(e))

############################################
# _______________________PRINT NUMBERS WITH TIME AND DAY OF WHEN IMAGE WAS SENT_______________________#

try:
    chat_messages = html.findAll('div', attrs={"class": "vW7d1"})
    numbers = []
    period = ""
    for i in chat_messages:
        timer = i.find('div', attrs={"class": "_3_7SH Zq3Mc"})
        try:
            if len(timer.get_text()) > 0:
                period = timer.get_text()
                # print "0:%s"%period
        except:
            pass
        a = i.findAll('img')
        if len(a) > 0:
            sender_name = i.find('span', attrs={"class": "_2a1Yw _1OmDL"})
            sender_number = i.find('span', attrs={"class": "RZ7GO"})
            if sender_name:
                day_with_name = "%s:%s" % (sender_name.get_text(), period)
                # print day_with_name
                numbers.append(day_with_name)
            if sender_number:
                day_with_number = "%s:%s" % (sender_number.get_text(), period)
                # print day_with_number
                numbers.append(day_with_number)
        else:
            pass
    # print numbers
except Exception as e:
    print "Exception was caused at getting number and day as %s" % (str(e))

#############################################

time.sleep(2)

###########################################
# _______________________IMAGES FROM CHAT THAT IS OPEN_______________________#

try:
    all_images_in_chat = html.findAll('div', attrs={"class": "_9tCEa"})
    image_in_chat = all_images_in_chat[0].find_all('img')
    src_urls = []
    for i in range(len(image_in_chat)):
        # print image_in_chat[i]['src']
        src_urls.append(image_in_chat[i]['src'])
except Exception as e:
    print "Exception was caused at getting images from chats as %s" % (str(e))

#######################################################################################
# _______________________TIME OF THE IMAGES ONLY_______________________#
try:
    AMPM = []
    hours = all_images_in_chat[0].find_all('div', attrs={"class": "_1DZAH _2Pjvv"})
    for i in hours:
        for j in i:
            for k in j:
                AMPM.append(k)
except Exception as e:
    print "Exception was caused at getting time of images only as %s" % (str(e))


################################################################################
# _______________________DOWNLOAD BLOB LINK IMAGES FUNCTION_______________________#

def get_file_content_chrome(driver, uri):
    result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
    # print "entered function"
    if type(result) == int:
        raise Exception("Request failed with status %s" % result)
    return base64.b64decode(result)


###################################################################################
# _______________________IMAGE DOWNLOAD WITH NUMBER WITH DAY AND TIME_______________________#
now = datetime.datetime.now()
folder_name = "%s-%s-%s at %s:%s:%s"%(now.day,now.month,now.year,now.hour,now.minute,now.second)
# path = "/home/tanmay/Desktop/Whatsapp/%s"%(folder_name)
print numbers
print AMPM
try:
    print "Final Code"
    for i in range(len(src_urls)):
        # print numbers[i]
        img_url = src_urls[i]
        bytes = get_file_content_chrome(driver, img_url)
        try:
            if os.makedirs("/home/tanmay/Desktop/Whatsapp/%s"%folder_name):
                pass
        except:
            pass
        # image_name = "%s : %s at %s .jpg" % (i + 1, numbers[i], AMPM[i])
        # path = os.path.join(path,image_name)
        file = open("/home/tanmay/Desktop/Whatsapp/%s/%s : %s at %s .jpg" % (folder_name, i + 1, numbers[i], AMPM[i]), "w")
        file.write(bytes)
        file.close()

    print "Code Ends"
except Exception as e:
    print "Exception was caused at downloading images as %s" % (str(e))

# print len(numbers)
# print len(AMPM)
#####################################################################################


# import json
# import time
# import urllib
# import base64
# import os.path
# import requests
# import datetime
# import BeautifulSoup
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support import expected_conditions as EC

# ######################################################################
# # _______________________HTML PARSING_______________________#
# try:
#     chrome_options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     driver.get("https://web.whatsapp.com/")
#     driver.set_window_size(20000, 12000)
#     time.sleep(10)
#     html = driver.page_source
#     html = BeautifulSoup(html)
# except Exception as e:
#     print "Exception was caused at HTML Parsing as %s" % (str(e))

# ##############################################################################
# # click using name of chat
# try:
#     name = raw_input("Enter Chat name correctly:\n")
#     number_to_scroll_up = int(raw_input("Enter number for scrolling as per estimated chat messages\n"))
#     n = number_to_scroll_up * (0.2)
#     name_path = "//span[@title='%s']" % (name)
#     # print name_path
#     time.sleep(3)
#     print "Clicking on Chat"
#     click_event = driver.find_element_by_xpath(name_path)
#     time.sleep(2)
#     click_event.click()
# except Exception as e:
#     print "Exception was caused at Clicking chat name as %s" % (str(e))

# ################################################################

# time.sleep(2)

# time.sleep(2)

# ##############################################
# # Scroll
# print "Scrolling"
# try:
#     move_to = driver.find_element_by_css_selector("body ._2nmDZ")

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(4)

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(4)

#     for i in range(number_to_scroll_up):
#         move_to.send_keys(Keys.HOME)
#         time.sleep(1)

#     time.sleep(n)

#     for i in range(20):
#         move_to.send_keys(Keys.HOME)
# except Exception as e:
#     print "Exception was caused at Scrolling as %s" % (str(e))

# ###########################################################################################
# # _______________________TO GET HTML ELEMENTS FROM NEWLY LOADED PAGE_______________________#
# try:
#     time.sleep(2)
#     html1 = driver.page_source
#     html = BeautifulSoup(html1)
#     # soup = BeautifulSoup(html, 'html.parser')
# except Exception as e:
#     print "Exception was caused at Parsing newly loaded HTML elements as %s" % (str(e))

# ############################################
# # _______________________PRINT NUMBERS WITH TIME AND DAY OF WHEN IMAGE WAS SENT_______________________#

# try:
#     chat_messages = html.findAll('div', attrs={"class": "vW7d1"})
#     numbers = []
#     period = ""
#     for i in chat_messages:
#         timer = i.find('div', attrs={"class": "_3_7SH Zq3Mc"})
#         try:
#             if len(timer.get_text()) > 0:
#                 period = timer.get_text()
#                 # print "0:%s"%period
#         except:
#             pass
#         a = i.findAll('img')
#         if len(a) > 0:
#             sender_name = i.find('span', attrs={"class": "_2a1Yw _1OmDL"})
#             sender_number = i.find('span', attrs={"class": "RZ7GO"})
#             if sender_name:
#                 day_with_name = "%s:%s" % (sender_name.get_text(), period)
#                 # print day_with_name
#                 numbers.append(day_with_name)
#             if sender_number:
#                 day_with_number = "%s:%s" % (sender_number.get_text(), period)
#                 # print day_with_number
#                 numbers.append(day_with_number)
#         else:
#             pass
#     # print numbers
# except Exception as e:
#     print "Exception was caused at getting number and day as %s" % (str(e))

# #############################################

# time.sleep(2)

# ###########################################
# # _______________________IMAGES FROM CHAT THAT IS OPEN_______________________#

# try:
#     all_images_in_chat = html.findAll('div', attrs={"class": "_9tCEa"})
#     image_in_chat = all_images_in_chat[0].find_all('img')
#     src_urls = []
#     for i in range(len(image_in_chat)):
#         # print image_in_chat[i]['src']
#         src_urls.append(image_in_chat[i]['src'])
# except Exception as e:
#     print "Exception was caused at getting images from chats as %s" % (str(e))

# #######################################################################################
# # _______________________TIME OF THE IMAGES ONLY_______________________#
# try:
#     AMPM = []
#     hours = all_images_in_chat[0].find_all('div', attrs={"class": "_1DZAH _2Pjvv"})
#     for i in hours:
#         for j in i:
#             for k in j:
#                 AMPM.append(k)
# except Exception as e:
#     print "Exception was caused at getting time of images only as %s" % (str(e))


# ################################################################################
# # _______________________DOWNLOAD BLOB LINK IMAGES FUNCTION_______________________#

# def get_file_content_chrome(driver, uri):
#     result = driver.execute_async_script("""
#     var uri = arguments[0];
#     var callback = arguments[1];
#     var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
#     var xhr = new XMLHttpRequest();
#     xhr.responseType = 'arraybuffer';
#     xhr.onload = function(){ callback(toBase64(xhr.response)) };
#     xhr.onerror = function(){ callback(xhr.status) };
#     xhr.open('GET', uri);
#     xhr.send();
#     """, uri)
#     # print "entered function"
#     if type(result) == int:
#         raise Exception("Request failed with status %s" % result)
#     return base64.b64decode(result)


# ###################################################################################
# # _______________________IMAGE DOWNLOAD WITH NUMBER WITH DAY AND TIME_______________________#
# now = datetime.datetime.now()
# folder_name = "%s-%s-%s at %s:%s:%s"%(now.day,now.month,now.year,now.hour,now.minute,now.second)
# path = "/home/tanmay/Desktop/Whatsapp/%s"%(folder_name)
# try:
#     print "Final Code"
#     for i in range(len(src_urls)):
#         # print numbers[i]
#         img_url = src_urls[i]
#         bytes = get_file_content_chrome(driver, img_url)
#         # image_name = "%s : %s at %s .jpg" % (i + 1, numbers[i], AMPM[i])
#         # path = os.path.join(path,image_name)
#         file = open("%s : %s at %s .jpg" % (i + 1, numbers[i], AMPM[i]), "w")
#         file.write(bytes)
#         file.close()

#     print "Code Ends"
# except Exception as e:
#     print "Exception was caused at downloading images as %s" % (str(e))

# # print len(numbers)
# # print len(AMPM)
# #####################################################################################