import time
from webbot import Browser
driver=Browser()

# set all the variables to your needs

period=3000 # the time period is 3200 seconds in my institute so I chose a lesser value than that
login_url=""
username=""
password=""
username_element_id="ft_un"
password_element_id="ft_pd"

# command line output

print("This program will keep running infinitely.")
print("It will refresh your login page after every",period, "seconds.")
print("Press CTRL+C to exit whenever you want.")

# process begins

driver.go_to(login_url)
driver.click(id=username_element_id)
driver.type(text=username, id=username_element_id)
driver.click(id=password_element_id)
driver.type(text=password, id=password_element_id)
driver.press(driver.Key.ENTER)

# sleep for period seconds and refresh

while(1):
    time.sleep(period)
    driver.refresh()
