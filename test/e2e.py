
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_scores_service(application_url="http://127.0.0.1:8777/"):
    # Create a WebDriver instance (assuming you have installed Selenium and have a compatible browser driver)
    driver = webdriver.Chrome()  # You may need to adjust this based on your setup

    try:
        # Open the provided URL
        driver.get(application_url)

        # Wait for the score element to be loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))

        # Find the score element
        score_element = driver.find_element_by_id('score')

        # Get the text content of the score element
        score_text = score_element.text

        # Check if the score is a number between 1 and 1000
        try:
            score = int(score_text)
            if 1 <= score <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False

    except TimeoutException:
        # If the score element is not found within the timeout period, return False
        return False

    finally:
        # Close the WebDriver instance
        driver.quit()


def main_function(application_url="http://127.0.0.1:8777/"):
    if test_scores_service(application_url):
        print("Success")
        return 0  # Tests passed
    else:
        print("Failed")
        return -1  # Tests failed
