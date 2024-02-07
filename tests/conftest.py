import pytest
from selene import browser


@pytest.fixture()
def mobile_browser_settings():
    browser.config.window_width = 414
    browser.config.window_height = 896

    yield

    browser.quit()


@pytest.fixture()
def desktop_browser_settings():
    browser.config.window_width = 1600
    browser.config.window_height = 950

    yield

    browser.quit()


@pytest.fixture(params=[(414, 896), (430, 932), (1600, 935), (1920, 1028)])
def desktop_mobile_settings(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()