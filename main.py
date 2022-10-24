from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import random


def click_to_cart():
    driver = webdriver.Chrome()
    driver.get('https://www.dodopizza.ru/moscow')
    time.sleep(10)
    with open("index_selenium10.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    with open("index_selenium10.html", "r", encoding="utf-8") as file:
        file = file.read()

    soup = BeautifulSoup(file, "lxml")
    pars_pizza_button = soup.find('section', id="pizzas", class_="sc-1n2d0ov-2 bxiXBh").find_all('article')
    list_butt = []
    for i in pars_pizza_button:
        i = str(i).split()
        if '><' in i[3]:
            i = i[3].split('><')
            list_butt.append(i[0])

    for i in range(4):
        button = driver.find_element(By.CSS_SELECTOR, f'[{random.choice(list_butt)}]')
        button.click()
        time.sleep(10)
        button2 = driver.find_element(By.CSS_SELECTOR, '[class="sc-1rmt3mq-0 cpUbDl gsrbdo-22 gaQAWN"]')
        button2.click()
        time.sleep(10)

    while True:
        print('Хотите закрыть, нажмите "y"')
        if input().lower() == "y":
            driver.close()
            driver.quit()
            break


def main():
    click_to_cart()


if __name__ == '__main__':
    main()
