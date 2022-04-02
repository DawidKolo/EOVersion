import os
from selenium import webdriver

os.environ['PATH'] += r"'..\'"
driver = webdriver.Chrome()
print("**************************************************************")
print("*                                                            *")
print("*           This script has been created by                  *")
print("*                   Dawid Kolodziej                          *")
print("*     source code: https://github.com/DawidKolo/EOVersion    *")
print("*       It is FREE to use by Precisely Support               *")
print("*                                                            *")
print("**************************************************************")

url = "https://support.precisely.com/products/"

server = url+'engageone-server/'
deliver = url+'engageone-deliver/'
generate = url+'engageone-generate/'
designer = url+'engageone-designer/'
vault = url+'engageone-vault/'
enrichment = url+'engageone-enrichment/'
CA = url+'engageone-content-author/'
smartBill = url+'engageone-smart-bill/'
PD = url+'portrait-dialogue/'
InterAct = url+'engageone-interactive/'

prod = [server, deliver, generate, designer, vault, enrichment, CA, smartBill, PD, InterAct]
pr = ["SERVER", "DELIVER", "GENERATE", "DESIGNER", "VAULT", "ENRICHMENT", "CONTENT-AUTHOR", "SMART-BILL",
          "PORTRAIT-DIALOGUE", "Interactive"]
a = []
for n in prod:
    driver.get(n)
    select_box = driver.find_elements_by_xpath("//select[@id='version']")

    # select_box = driver.find_elements(by=By.XPATH, value="//select[@id='version']")

    for item in select_box:
        x= item.get_attribute('value')
        a.append(x)

res = "\n".join("{} {}".format(x, y) for x, y in zip(pr, a))
print(res)



driver.quit()
