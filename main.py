import os
from selenium import webdriver

os.environ['PATH'] += r"'..\'"
driver = webdriver.Chrome()

server = 'https://support.precisely.com/products/engageone-server/'
deliver = 'https://support.precisely.com/products/engageone-deliver/'
generate = 'https://support.precisely.com/products/engageone-generate/'
designer = 'https://support.precisely.com/products/engageone-designer/'
vault = 'https://support.precisely.com/products/engageone-vault/'
enrichment = 'https://support.precisely.com/products/engageone-enrichment/'
CA = 'https://support.precisely.com/products/engageone-content-author/'
smartBill = 'https://support.precisely.com/products/engageone-smart-bill/'
PD = 'https://support.precisely.com/products/portrait-dialogue/'
prod = [server, deliver, generate, designer, vault, enrichment, CA, smartBill, PD]

print("**************************************************************")
print("*                                                            *")
print("*           This script has been created by                  *")
print("*                   Dawid Kolodziej                          *")
print("*     source code: https://github.com/DawidKolo/EOVersion    *")
print("*       It is FREE to use by Precisely Support               *")
print("*                                                            *")
print("**************************************************************")

for n in prod:
    driver.get(n)

    select_box = driver.find_elements_by_xpath("//select[@id='version']")

    # select_box = driver.find_elements(by=By.XPATH, value="//select[@id='version']")

    for item in select_box:
        print(n + ' ' + item.get_attribute('value'))

driver.quit()