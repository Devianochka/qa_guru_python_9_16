"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene import browser, be


@pytest.fixture(params=[(414, 896), (430, 932), (1600, 935), (1920, 1028)])
def window_size(request):
    width, heigth = request.param
    browser.config.window_width = width
    browser.config.window_height = heigth
    if width <= 1011:
        return 'mobile'
    if width >= 1012:
        return 'desktop'


def test_github_desktop(window_size):
    if window_size == 'mobile':
        pytest.skip('mobile window size')
    browser.open('https://github.com/')

    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)


def test_github_mobile(window_size):
    if window_size == 'desktop':
        pytest.skip('desktop window size')
    browser.open('https://github.com/')

    browser.element('[class*="toggle-bar"]').click()
    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)