from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developer\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# timeout = time.time() + 60*0.3

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)


thirty_sec=time.time()+30
timeout = time.time()+3

while thirty_sec > time.time():
    driver.find_element_by_id("cookie").click()
    if time.time() > timeout:

        #Convert <b> text into an integer price.
        all_price = driver.find_elements_by_css_selector("#store b")
        right_side_price = []
        for price in all_price:
            external = price.text
            if external != "":
                cost = int(external.split("-")[1].strip().replace(",", ""))
                right_side_price.append(cost)

        # Create dictionary of store items and prices
        cookies_upgrade = {}
        for i in range(len(right_side_price)):
            cookies_upgrade[right_side_price[i]] = item_ids[i]

        ##Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        print(f"cookies cost is {cookie_count}")

        # Find upgrades that we can currently afford
        affordable_cookies={}
        for cost,id in cookies_upgrade.items():
            if cookie_count>cost:
                affordable_cookies[cost] = id

        # Purchase the most expensive affordable upgrade
        higest_value = max(affordable_cookies)
        print(higest_value)
        to_purchase_id = affordable_cookies[higest_value]

        driver.find_element_by_id(to_purchase_id).click()
        
        #Add Another five second
        timeout=time.time()+3

final_rate = driver.find_element_by_id("cps")
print(final_rate.text)