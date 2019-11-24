from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"..\drivers\chromedriver.exe")
#driver = webdriver.edge(r"..\drivers\msedgedriver.exe")

# FONCTIONNEMENT DE LA RECHERCHE VIA GOOGLE, tout peut se faire remplacer en mettant driver.get("youtube')

# driver.set_page_load_timeout(10)
# driver.get("https://www.google.fr/") #Aller chercher google.fr
# driver.find_element_by_name("q").send_keys("Youtube")  # q = barre de recherche
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  # btnK = bouton rechercher / faire l'action appuyer sur entrée
# driver.find_element_by_class_name("S3Uucc").click()

driver.get("https://www.youtube.com/?hl=fr&gl=FR")

driver.find_element_by_name("search_query").send_keys("Squeezie")
time.sleep(2)
driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
#driver.maximize_window()
driver.find_element_by_class_name("style-scope ytd-channel-name").click()


print("test completed succesfully")

