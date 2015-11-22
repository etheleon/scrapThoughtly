#!/usr/bin/env python

import beautifulsoup4 as bs
import selenium

username = selenium.find_element_by_id("username")
password = selenium.find_element_by_id("password")

username.send_keys("YourUsername")
password.send_keys("Pa55worD")

selenium.find_element_by_name("submit").click()
