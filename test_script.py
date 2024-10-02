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
        
        # Fetch the page title
        title = driver.title.strip()  # Strip spaces for comparison
        print(f"Page Title is: '{title}'")

        # Assert that part of the expected title is present
        assert "Exclusive Exam Papers With Answers" in title, "Title does not match!"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_example()
