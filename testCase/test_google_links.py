#! /usr/bin/env python
# coding:utf-8

# auther: hython

from selenium import webdriver
import unittest


class GoogleLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.dirver.get('https://www.google.com')

    def tearDown(self):
        self.driver.quit()

    def test_google_news(self):
        '''toppage -> news page'''
        self.driver.find_element_by_link_text('news').click()
        self.assertEqual(self.driver.current_url, 'https://news.google.com')

    def test_google_map(self):
        '''toppage -> map page'''
        self.driver.find_element_by_link_text('map').click()
        self.assertEqual(self.driver.current_url, 'https://map.google.com')


if __name__ == '__main__':
    unittest.main(verbosity=2)
