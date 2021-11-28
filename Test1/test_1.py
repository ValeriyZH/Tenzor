from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import sys
import os

sys.path.append(os.path.abspath('/home/gm/PycharmProjects/Test1/'))
from base_page import BasePage as Base
from selectorss import Selectorss as S
from data import Data as D
from loguru import logger


def __init__(self, browser):
    self.browser = browser



@logger.catch
def test_primer(browser):
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ КОМПАНИИ TENSOR.RU')

    logger.info('# установили максимальный размер окна браузера')
    # browser.set_window_size (D.windows_width, D.windows_high)
    browser.maximize_window()

    logger.info('Тестовое задание 1 "Поиск в Яндексе".')
    message_in_log = '# заходим на тестовую страницу' + D.url_yandex
    logger.info(message_in_log)
    browser.get(D.url_yandex)

    logger.info('# проверяем наличие поля поиска')
    Base.element_exists_and_click(browser, S.xpath_yandex_search)

    logger.info('# вводим в строку поиска слово "Тензор"')
    Base.element_exists_and_send(browser, S.xpath_yandex_search, D.search_string)

    logger.info('# проверяем наличие таблицы подсказок suggest')
    Base.element_exists_and_click(browser, S.xpath_yandex_search)

    logger.info('# нажимаем клавишу "Enter"')
    Base.element_exists_and_click_enter(browser, S.xpath_yandex_search)

    logger.info('# получаем список первых пяти ссылок:')
    Tenzor_array = Base.element_exists_array(browser, S.xpath_elements2)
    for i in range(D.elements_count):
        links_text = Tenzor_array[i].get_attribute("href")
        logger.info('#   ' + links_text)

    message_in_log = '# проверяем, есть ли в них ' + D.tenzor_site
    logger.info(message_in_log)
    links_count = 0
    for i in range(D.elements_count):
        links_text = Tenzor_array[i].get_attribute("href")
        if D.tenzor_site in links_text:
            links_count += 1
    message_in_log = '# всего  ' + D.tenzor_site + ' есть в ' + str(links_count) + ' из ' + str(D.elements_count)
    logger.info(message_in_log)

    logger.info('# успеваем посмотреть на результат поиска в браузере')

    logger.info('Завершили тестовое задание 1 "Поиск в Яндексе".')

    time.sleep(7)
