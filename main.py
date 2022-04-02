import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"'..\'"
driver = webdriver.Chrome()
line = "**************************************************************"
space = "*                                                            *"
print(line)
print(space)
print("*           This script has been created by                  *")
print("*                   Dawid Kolodziej                          *")
print("*     source code: https://github.com/DawidKolo/EOVersion    *")
print("*       It is FREE to use by Precisely Support               *")
print(space)
print(line)

url = "https://support.precisely.com/products/engageone"

server = url+'-server/'
deliver = url+'-deliver/'
generate = url+'-generate/'
designer = url+'-designer/'
vault = url+'-vault/'
enrichment = url+'-enrichment/'
CA = url+'-content-author/'
smartBill = url+'-smart-bill/'
PD = 'https://support.precisely.com/products/portrait-dialogue/'
InterAct = url+'-interactive/'

prod = [server, deliver, generate, designer, vault, enrichment, CA, smartBill, InterAct, PD]
pr = ["SERVER", "DELIVER", "GENERATE", "DESIGNER", "VAULT", "ENRICHMENT", "CONTENT-AUTHOR", "SMART-BILL",
           "INTERACTIVE", "PORTRAIT-DIALOGUE"]
a = []
for n in prod:
    driver.get(n)

    select_box = driver.find_elements(by=By.XPATH, value="//select[@id='version']")

    for item in select_box:
        x= item.get_attribute('value')
        a.append(x)

res = "\n".join("{} {}".format(x, y) for x, y in zip(pr, a))
print(res)

driver.quit()
