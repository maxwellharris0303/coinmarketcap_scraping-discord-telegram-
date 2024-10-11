from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

def scroll_down(driv):
    page_height = driv.execute_script("return document.body.scrollHeight")
    scroll_distance = page_height // 5
    driv.execute_script(f"window.scrollTo(0, {scroll_distance});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance}, {scroll_distance * 2});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 2}, {scroll_distance * 3});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 3}, {scroll_distance * 4});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 4}, {page_height});")

url = "https://coinmarketcap.com/"

driver = webdriver.Chrome()
driver.get(url)

# WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"onetrust-accept-btn-handler\"]"))).click()
sleep(3)

index=  100
for i in range(index):
    try:
        scroll_down(driver)

        rows = driver.find_elements(By.TAG_NAME, "tr")
        rows.pop(0)
        all_links = []
        for row in rows:
            link = row.find_element(By.TAG_NAME, "a").get_attribute('href')
            print(link)
            all_links.append(link)
            with open('urls.txt', 'a') as file:
                # Write the string to the file
                file.write(link + "\n")


        pagination_element = driver.find_element(By.CSS_SELECTOR, "ul[class=\"pagination\"]")
        driver.execute_script("arguments[0].scrollIntoView(false);", pagination_element)

        next_page_button = pagination_element.find_element(By.CSS_SELECTOR, "li[class=\"next\"]")
        driver.get(next_page_button.find_element(By.TAG_NAME, "a").get_attribute('href'))   
    except:
        pass
        sleep(2)
    
    
print(len(all_links))