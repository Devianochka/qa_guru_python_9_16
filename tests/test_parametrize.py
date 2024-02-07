"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be


@pytest.mark.parametrize("desktop_mobile_settings", [(1600, 935), (1920, 1028)], indirect=True)
def test_github_desktop(desktop_mobile_settings):
    browser.open('https://github.com/')

    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)


@pytest.mark.parametrize("desktop_mobile_settings", [(414, 896), (430, 932)], indirect=True)
def test_github_mobile(desktop_mobile_settings):
    browser.open('https://github.com/')

    browser.element('[class*="toggle-bar"]').click()
    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)