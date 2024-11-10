
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

# Function to start Selenium automation
def start_automation(topic):
    driver = webdriver.Chrome()  # Or use Firefox with webdriver.Firefox()
    driver.get("https://www.instagram.com/")

    # Login to Instagram
    login_instagram(driver)

    # Interact with the given topic
    interact_with_topic(driver, topic)

    driver.quit()

# Function to log in to Instagram
def login_instagram(driver):
    username = ""
    password = ""
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    try:
        # Locate the username and password fields by their 'name' attribute
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        
        # Fill in the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(5)  # Wait for login to complete

        # If there's a "Save Your Login Info" popup, click "Not Now"
        try:
            not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
            not_now_button.click()
            time.sleep(2)
        except Exception as e:
            print("No 'Save Your Login Info' popup.")

        # If there's a "Turn on Notifications" popup, click "Not Now"
        try:
            not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
            not_now_button.click()
            time.sleep(2)
        except Exception as e:
            print("No 'Turn on Notifications' popup.")
    
    except Exception as e:
        print(f"Error during login: {e}")
        driver.quit()

# Function to interact with the specified topic
def interact_with_topic(driver, topic):
    search_url = f"https://www.instagram.com/explore/tags/{topic}/"
    driver.get(search_url)
    time.sleep(3)

    for i in range(5):  # Scroll and like posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        like_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='Like']")
        for btn in like_buttons:
            btn.click()
            time.sleep(1)

# Function to run the automation in a separate thread
def run_automation():
    topic = entry.get()
    threading.Thread(target=start_automation, args=(topic,)).start()

# Create Tkinter window
root = tk.Tk()
root.title("Instagram Automation")

# Create Label and Entry widget
label = tk.Label(root, text="Enter Topic:")
label.pack(padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

# Create a Button to trigger the automation
button = tk.Button(root, text="Start Automation", command=run_automation)
button.pack(padx=10, pady=10)

# Run Tkinter event loop
root.mainloop()
