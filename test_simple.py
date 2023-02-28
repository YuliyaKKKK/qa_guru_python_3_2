
from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 1100


def test_one(open_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second(open_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('Marg').press_enter()
    browser.element('[id="search"]').should_not(have.text('Selene - User-oriented Web UI browser tests in Python'))
