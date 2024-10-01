from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_example():
    # Use Chrome as the web driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        # Open a website
        driver.get("https://www.smoothmaths.co.uk")
        
        # Example of interacting with a webpage
        title = driver.title
        print("Page Title is: " + title)

        # Assert the title is correct
        assert "https://www.smoothmaths.co.uk" in title

    finally:
        driver.quit()

if __name__ == "__main__":
    test_example()
