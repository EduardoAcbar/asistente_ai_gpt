# Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=C:\Selenium\EdgeProfile"
#PS C:\Program Files (x86)\Microsoft\Edge\Application>
#Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=C:\Selenium\EdgeProfile"
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

def interact_with_website(mensaje):
    # Specify the debugger address (Edge is running on port 9222)
    edge_options = Options()
    edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # Launch WebDriver with these options
    driver = webdriver.Edge(options=edge_options)

    # Wait for the page to load (you may adjust this)
    time.sleep(5)

    try:
        # Find the input element using XPath and enter the message
        input_xpath = "/html/body/div[1]/div/main/div[1]/div[1]/div/div[2]/div/div/div/div[4]/form/div/div/div[2]/div/div/div/div/p"
        input_element = driver.find_element(By.XPATH, input_xpath)
        input_element.send_keys(mensaje)

        # Wait for 3 seconds
        time.sleep(3)

        # Click the button to submit
        button_xpath = "/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[2]/div/div/div/div[4]/form/div/div/div[2]/div/div[2]/button"
        button_element = driver.find_element(By.XPATH, button_xpath)
        button_element.click()

        # Wait for 3 seconds
        time.sleep(3)

        # Loop through and click copy button, then print copied text
        for i in range(2, 8, 2):  # Start at 2, go up to 6, increment by 2
            copy_button_xpath = f"/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div/article[{i}]/div/div/div[2]/div/div[2]/div/div/span[1]/button"
            copy_button_element = driver.find_element(By.XPATH, copy_button_xpath)
            copy_button_element.click()
            print(f"Clicked copy button in article[{i}]")

            # Wait to ensure the text is copied
            time.sleep(2)

            # Get the copied text using pyperclip
            copied_text = pyperclip.paste()
            print(f"Copied text from article[{i}]: {copied_text}")

            # Wait for 3 seconds before the next iteration
            time.sleep(3)

    finally:
        driver.quit()  # Close the WebDriver session

texto = "Hola"
# Call the function
interact_with_website(texto)
