import tkinter as tk
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def find_element(driver, locator):
    """
    Finds an element in the web driver using a locator.

    Arguments:
    driver -- the web driver instance
    locator -- a tuple containing the locator method and the locator value

    Returns:
    The web element if found, or None if not found
    """
    try:
        method, value = locator
        if method == By.ID:
            element = driver.find_element(By.ID, value)
        elif method == By.NAME:
            element = driver.find_element(By.NAME, value)
        elif method == 'class name':
            element = driver.find_element(By.CLASS_NAME, value)
        elif method == By.XPATH:
            element = driver.find_element(By.XPATH, value)
        elif method == By.CSS_SELECTOR:
            element = driver.find_element(By.CSS_SELECTOR, value)
        else:
            raise ValueError(f"Invalid locator method: {method}")
        return element
    except NoSuchElementException:
        return None

def on_find():
    """
    Finds an element in the web driver using the locator values from the GUI and displays the result.
    """
    method = method_entry.get()
    value = value_entry.get()
    locator = (method, value)
    element = find_element(driver, locator)
    if element:
        result_label.config(text=f"Element found: {element.text}")
    else:
        result_label.config(text="Element not found")

# Create the main window
window = tk.Tk()
window.title("Element Finder")

# Create the input fields
method_label = tk.Label(window, text="Locator Method:")
method_label.pack()
method_entry = tk.Entry(window)
method_entry.pack()

value_label = tk.Label(window, text="Locator Value:")
value_label.pack()
value_entry = tk.Entry(window)
value_entry.pack()

# Create the find button
find_button = tk.Button(window, text="Find", command=on_find)
find_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create the web driver
executable_path = "C:\webdriver\chromedriver.exe"
try:
    driver = webdriver.Chrome(executable_path=executable_path)
except:
    driver = webdriver.chrome()
driver.get("https://www.google.com")

# Start the main loop
window.mainloop()

# Quit the web driver
driver.quit()
