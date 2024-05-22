import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def worker():
    options = Options()
    options.add_argument("--disable-cache")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.minimize_window()

    sli_do_url = "https://app.sli.do/event/a4ksNTUe3gLdtQTnEYJez8/live/questions?clusterId=eu1"
    element_xpath = "/html/body/div[4]/div[3]/div[2]/div[1]/div[2]/div[5]/div/div[1]/div/div/div[1]/div[3]/div[2]/button"

    while True:
        driver.get(sli_do_url)
        driver.find_element("xpath", "/html/body/div[4]/div/div[3]/form/div[1]/div/div/input").send_keys("Bot 1")
        driver.find_element("xpath", "/html/body/div[4]/div/div[3]/form/label/span[1]/span/input").click()
        driver.find_element("xpath", "/html/body/div[4]/div/div[3]/form/div[2]/button").click()
        driver.find_element("xpath", element_xpath).click()
        driver.get("data:,")
        driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
            "origin": '*',
            "storageTypes": 'all',
        })


num_threads = int(input("Threads: "))
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker, name=f"Worker-{i + 1}")
    thread.start()
    threads.append(thread)
    time.sleep(0.1)

for thread in threads:
    thread.join()
