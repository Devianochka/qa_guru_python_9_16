"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, be


def test_github_desktop(desktop_browser_settings):
    browser.open('https://github.com/')

    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)


def test_github_mobile(mobile_browser_settings):
    browser.open('https://github.com/')

    browser.element('[class*="toggle-bar"]').click()
    browser.element('[class*=sign-in]').click()

    browser.element('#login').should(be.visible)