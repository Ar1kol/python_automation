import os
import sys
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

app_path = os.path.dirname(sys.executable)

website = "https://www.thesun.co.uk/sport/football/"
chrome_driver_path = "chromedriver.exe"

# headless-mode
options_parameters = Options()
options_parameters.headless = True

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service, options=options_parameters)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []


for container in containers:
    titles.append(container.find_element(by="xpath", value='./a/h3').text)
    subtitles.append(container.find_element(by="xpath", value='./a/p').text)
    links.append(container.find_element(by="xpath", value='./a').get_attribute("href"))


file_name = f"headline-{datetime.now().strftime('%d/%m/%Y')}.csv" #DDMMYYYY
final_path = os.path.join(app_path, file_name)

df_headlines = pd.DataFrame({"titles":titles, "subtitles":subtitles, "links":links})
df_headlines.to_csv(final_path)

driver.quit()