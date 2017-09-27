#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title