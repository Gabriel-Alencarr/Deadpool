import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)


def check_exists_by_css_selector(driver: WebDriver, selector: str) -> bool:
    try:
        driver.find_element(
            By.CSS_SELECTOR, selector
            )
    except NoSuchElementException:
        return False
    return True


def scroll_down(driver: WebDriver, pause_time: int = 1) -> None:
    last_height = driver.execute_script(
        "return document.body.scrollHeight"
        )

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
            )
        time.sleep(pause_time)

        try:
            search_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, "#loadMore"
                    ))
            )
            driver.execute_script(
                "arguments[0].click();", search_btn
                )
            time.sleep(2)
        except NoSuchElementException:
            print("Botão 'loadMore' não encontrado.")
            break
        except Exception as e:
            print(f"Erro ao clicar no botão 'loadMore': {e}")
            break
        new_height = driver.execute_script(
            "return document.body.scrollHeight"
            )
        if new_height == last_height:
            break
        last_height = new_height


try:
    driver.get("https://www.omelete.com.br")
    search_icon = driver.find_element(
        By.CSS_SELECTOR, "i.icon-search"
        )
    search_icon.click()
    time.sleep(1)

    search_input = driver.find_element(
        By.CSS_SELECTOR, 'input[name="q"]'
        )
    search_input.send_keys("Deadpool")
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    
    scroll_down(driver)
    time.sleep(2)
    
    news_elements = driver.find_elements(
        By.CSS_SELECTOR, ".c-newslist article"
        )
    with open("deadpool_news.txt", "w", encoding="utf-8") as file:
        for news in news_elements:
            title = news.find_element(
                By.CSS_SELECTOR, "h2"
                ).text
            date = news.find_element(
                By.CSS_SELECTOR, ".mark__time"
                ).text
            file.write(f"Título: {title}\n")
            file.write(f"Data: {date}\n")
            file.write("\n")

except Exception as error:

    print(f"Erro: {str(error)}")

finally:
    driver.quit()