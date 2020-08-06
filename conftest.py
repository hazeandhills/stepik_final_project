import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: ru\en etc...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language") 
    browser = None
    if language == "ru" or "es" or "ar" or "ca" or "cs" or "da" or "de" or "en-gb" or "el" or "fi" or "fr" or "it" or "ko" or "nl" or "pl" or "pt" or "pt-br" or "ro" or "sk" or "uk" or "zh-cn":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be choosen")
    yield browser
    print("\nquit browser..")
    browser.quit()