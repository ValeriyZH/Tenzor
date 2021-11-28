import datetime
import os
import sys
import time

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

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ 2 ДЛЯ КОМПАНИИ TENSOR.RU')

    logger.info('# установили максимальный размер окна браузера')
    # browser.set_window_size (D.windows_width, D.windows_high)
    browser.maximize_window()

    logger.info('Тестовое задание 2 "Картинки на Яндексе".')

    message_in_log = '# заходим на тестовую страницу' + D.url_yandex
    logger.info(message_in_log)
    browser.get(D.url_yandex)

    logger.info('# проверяем наличие ссылки и переходим на "Картинки"')
    Base.element_exists_and_click(browser, S.xpath_yandex_image_link)

    time.sleep(3)

    logger.info('# делаем открывшуюся вкладку основной и активной, закрываем старую вкладку')
    Base.switch_to_current_window(browser)

    logger.info('# сейчас текущий upl:')
    url = browser.current_url
    message_in_log = '# ' + str(url)
    logger.info(message_in_log)

    time.sleep(3)

    logger.info('# ищем в картинках "блюда из тыквы')
    Base.element_exists_and_send(browser, S.xpath_yandex_search_image5, D.search_in_image_string)
    Base.element_exists_and_click_enter(browser, S.xpath_yandex_search_image5)

    logger.info('# открываем первую картинку')
    Base.element_exists_and_click(browser, S.xpath_yandex_image1_pumpkin)

    time.sleep(3)

    link1 =  browser.current_url

    logger.info('# переходим на вторую картинку')
    Base.element_exists_and_click(browser, S.xpath_next_image_button)

    logger.info('# возвращаемся на первую картинку')
    Base.element_exists_and_click(browser, S.xpath_prev_image_button)

    time.sleep(3)

    link2 = browser.current_url

    logger.info('# ссылка первой картинки:')
    message_in_log = '# ' + str(link1)
    logger.info(message_in_log)

    logger.info('# ссылка первой картинки после возврата:')
    message_in_log = '# ' + str(link2)
    logger.info(message_in_log)

    if link1 == link2:
        logger.info('# ссылки одинаковые')
    else:
        logger.info('# ссылки разные!')

    logger.info('Завершили тестовое задание 2 "Картинки на Яндексе" ')

    time.sleep(7)
