import pytest
import time
import math
from selenium import webdriver

def get_feedback(browser):
    return browser.find_element_by_css_selector(".smart-hints__hint").text

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_feedback_message(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    input_field = browser.find_element_by_css_selector(".textarea")
    input_field.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    feedback = get_feedback(browser)
    assert feedback == "Correct!", f"Unexpected feedback: {feedback}"
