# Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=C:\Selenium\EdgeProfile"
#PS C:\Program Files (x86)\Microsoft\Edge\Application>
#Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=C:\Selenium\EdgeProfile"

import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

# Specify the debugger address (Edge is running on port 9222)
edge_options = Options()
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Launch WebDriver with these options
driver = webdriver.Edge(options=edge_options)

# Wait for the page to load (you may adjust this)
time.sleep(5)

# Find the input element using XPath and enter "Hola chatGPT"
input_xpath = "/html/body/div[1]/div/main/div[1]/div[1]/div/div[2]/div/div/div/div[4]/form/div/div/div[2]/div/div/div/div/p"
input_element = driver.find_element(By.XPATH, input_xpath)
input_element.send_keys("Hola chatGPT")

# Wait for 3 seconds
time.sleep(3)

# Click the button to submit (the button's SVG element)
button_xpath = "/html/body/div[1]/div/main/div[1]/div[1]/div/div[2]/div/div/div/div[4]/form/div/div/div[2]/div/button"
button_element = driver.find_element(By.XPATH, button_xpath)
button_element.click()

# Wait for 3 seconds
time.sleep(3)

# Loop through and change the value of "article[2]", "article[4]", etc.
for i in range(2, 8, 2):  # Start at 2, go up to 6, increment by 2
    copy_button_xpath = f"/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div/article[{i}]/div/div/div[2]/div/div[2]/div/div/span[1]/button"
    
    try:
        # Locate the copy button using the dynamic XPath and click it
        copy_button_element = driver.find_element(By.XPATH, copy_button_xpath)
        copy_button_element.click()
        print(f"Clicked copy button in article[{i}]")

        # Hotkey sequence: Alt+Tab, Ctrl+V, Alt+Tab
        time.sleep(1)  # Short delay to ensure the action is performed smoothly
        pyautogui.hotkey('alt', 'tab')  # Switch to the next window
        time.sleep(1)  # Short delay to ensure window switch is complete
        pyautogui.hotkey('ctrl', 'v')   # Paste the copied content
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab')  # Switch back to the original window
        send_xpath ="/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div[2]/div/div/div/div/p"
        send_element = driver.find_element(By.XPATH, send_xpath)
        send_element.send_keys("Hola chatGPT")

        flecha_xpath = "/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div[2]/div/button"
        flecha_element = driver.find_element(By.XPATH, flecha_xpath)
        flecha_element.click()
        print(f"Performed Alt+Tab, Ctrl+V, and Alt+Tab for article[{i}]")
        
    except Exception as e:
        print(f"Could not click copy button in article[{i}]: {e}")
    
    # Wait for 3 seconds before the next iteration
    time.sleep(3)


# Close the driver (optional)
# driver.quit()

#/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[2]/div/div/div[2]/div/div[2]/div/div/span[2]/button
#/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[4]/div/div/div[2]/div/div[2]/div/div/span[2]/button
#/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[6]/div/div/div[2]/div/div[2]/div/div/span[2]/button
#/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[8]/div/div/div[2]/div/div[2]/div/div/span[2]/button