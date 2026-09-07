from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
# To Keep Browser Open Indefinitely
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Edge(options=options, service=service_obj)
driver.maximize_window()
driver.get("http://localhost:5173/")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "text-sm").click()
driver.find_element(By.NAME, "email").send_keys("mkobir2310272@bscse.uiu.ac.bd")
driver.find_element(By.NAME, "password").send_keys("1234567888")
driver.find_element(By.CLASS_NAME, "btn ").click()


time.sleep(5)
driver.find_element(By.LINK_TEXT, "Post Ride").click()

time.sleep(2)

driver.find_element(By.CLASS_NAME, "btn-primary ").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "border").click()
time.sleep(5)

driver.find_element(By.CLASS_NAME, "border").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "bg-slate-900").click()




