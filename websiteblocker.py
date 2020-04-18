from datetime import datetime as dt
import time

host_path =r"hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com', 'messenger.com', 'www.messenger.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,20):
         print("Working Hours...")
         with open(host_path, 'r+') as file:
             content = file.read()
             for website in website_list:
                 if website in content:
                     pass
                 else:
                    file.write(redirect+" "+website+"\n")




    time.sleep(300)