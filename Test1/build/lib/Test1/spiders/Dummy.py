from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import re
import csv
import pandas as pd
import json
import scrapy
import time


class TestSpider2(scrapy.Spider):
    name = "result23"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
    allowed_domains = ["instagram.com"]
    handle_httpstatus_list = [999]  # without this line the crawler would stop

    # working since it ignores all the non 200 responses
    def start_requests(self):
        print("start time is ")
        print(time.time())

        
        username = "harshyadav19682023"
        password = "henrynicolls1"
        L = instaloader.Instaloader()
       # L.login(username , password)

        HASHTAG ="rentinwashington"

        df = pd.DataFrame()

        for post in L.get_hashtag_posts(HASHTAG):
            time.sleep(3)
            url1 = f"https://www.instagram.com/p/{post.shortcode}/"
            yield scrapy.Request(url1, callback=self.parse, cb_kwargs={'post' : post})

        print("end time is ")
        print(time.time())


    def parse(self, response , post):
         #print(response.url)
         post_likes=post.get_likes()
         post_comment = post.get_comments()


         comment_list=[]
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

                posturl_list.append(response.url)
                username_list.append(profile.username)
                fullname_list.append(profile.full_name)
                biography_list.append(profile.biography)
                followers_list.append(profile.followers)
                followee_list.append(profile.followees)
                np_list.append(profile.mediacount)
                profile_pic_list.append(profile.profile_pic_url)
                isprivate_list.append(profile.is_private)
                isverified_list.append(profile.is_verified)
                hasliked.append("True")
                hascommented.append(bool(var1))
                des_list.append(post.caption)



         df = pd.DataFrame({"URL of post": posturl_list, "description": des_list, "username": username_list,
                            "fullname":  fullname_list, "biography": biography_list,
                            "followers":  followers_list, "following": followee_list,
                            "Number of posts": np_list, "profile_pic_url": profile_pic_list,
                            "is_private": isprivate_list, "is_verified": isverified_list, "isliked":  hasliked,
                            "iscommented": hascommented})
         df.to_csv("Updated4.csv", mode='a')
         time.sleep(10)


