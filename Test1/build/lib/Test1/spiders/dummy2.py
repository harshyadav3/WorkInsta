from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import re
import csv
import pandas as pd
import json
import scrapy
import time
from ..items import Test1Item
import time

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait




class TestSpider2(scrapy.Spider):
    name = "result21"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
    allowed_domains = ["instagram.com"]
    handle_httpstatus_list = [999]  # without this line the crawler would stop

    # working since it ignores all the non 200 responses
    def start_requests(self):
        print("start time is ")
        print(time.time())

        username = "ranvijay722"
        password = "grand#father@@#"
        L = instaloader.Instaloader()
        L.login(username, password)

        HASHTAG = "rentinwashington"

        df = pd.DataFrame()

        '''
        L.context.log("Login...")
        L.load_session_from_file("harshyadav19682023")
        
        try:
            L = instaloader.Instaloader()
            L.login(username, password)
        except Exception as e:
            print(e)
            temp1 =e.split("-")[0]
            temp2 = temp1.split("to")[1]

            urlNew = temp2[25:]
            print(urlNew)
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome('/Users/username/bin/chromedriver', chrome_options=chrome_options)
            driver.get(urlNew)
            username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
            print(username)
            # enter username and password
            username.clear()
            username.send_keys("harshyadav19682023")
            password.clear()
            # use your username and password
            password.send_keys("henrynicolls1")
            # target the login button and click it
            time.sleep(2)
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            # We are logged in!
            print("Logged in")
            time.sleep(10)
            L.login(username, password)
        '''


        for post in L.get_hashtag_posts(HASHTAG):
            time.sleep(3)
            url1 = f"https://www.instagram.com/p/{post.shortcode}/"
            yield scrapy.Request(url1, callback=self.parse, cb_kwargs={'post': post})

        print("end time is ")
        print(time.time())

    def parse(self, response, post):
        print(response.url)
        post_likes = post.get_likes()
        post_comment = post.get_comments()
        items = Test1Item()
        comment_list = []
        posturl_list = []
        username_list = []
        fullname_list = []
        biography_list = []
        followers_list = []
        followee_list = []
        np_list = []
        profile_pic_list = []
        isprivate_list = []
        isverified_list = []
        hasliked = []
        hascommented = []
        des_list = []
        id_list = []

        for comment in post_comment:
            comment_list.append(comment.owner.username)

        for profile in post_likes:
            # print("Username:", profile.username)
            # print("Full Name:", profile.full_name)
            # print("Biography:", profile.biography)
            # print("Followers:", profile.followers)
            # print("Following:", profile.followees)
            # print("Number of Posts:", profile.mediacount)
            # print("Profile Picture URL:", profile.profile_pic_url)
            # print("Is Private:", profile.is_private)
            # print("Is Verified:", profile.is_verified)

            var1 = 0
            for x in comment_list:
                if (x == profile.username):
                    var1 = 1

                print("Username:", profile.username)
                print("Full Name:", profile.full_name)
                print("Following:", profile.followers)

            #items = Test1Item()
            items['Username'] =  profile.username,
            items['Fullname'] = profile.full_name,
            items['Followers'] = profile.followers,
            items['Following'] = profile.followees

            yield items




