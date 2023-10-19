import pytest
from selenium import webdriver

# Фікстура для автоматичного старту та завершення браузера
@pytest.fixture(scope="class", autouse=True)
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Тести
class TestWebsite:
    def test_open_website(self, browser):
        browser.get("https://www.google.com")
        assert "Google" in browser.title

    def test_math_addition(self):
        result = 2 + 3
        assert result == 5

    def test_string_length(self):
        text = "Hello, World!"
        assert len(text) == 13

if __name__ == "__main__":
    pytest.main()
