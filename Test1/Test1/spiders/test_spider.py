from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import re
import csv
import pandas as pd
import json
import scrapy
from scrapy.crawler import CrawlerProcess
import time




class TestSpider(scrapy.Spider):
    name = "result"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
    allowed_domains = ["instagram.com"]
    handle_httpstatus_list = [999]  # without this line the crawler would stop

    # working since it ignores all the non 200 responses
    def start_requests(self):
        print("start time ")
        #print(time())
        print(time.time())
        username = "harshyadav19682023"
        password = "henrynicolls1"
        L = instaloader.Instaloader()
        L.login(username, password)
        HASHTAG = "rentinnoida"

        like_list = []
        id = []
        url_post = []
        ld = ''
        profile_urls = []
        # owner2 = []
        comment_list = []
        posturl_list = []
        username_list=[]
        fullname_list=[]
        biography_list=[]
        followers_list=[]
        followee_list=[]
        np_list=[]
        profile_pic_list=[]
        isprivate_list=[]
        isverified_list=[]
        hasliked=[]
        hascommented=[]
        des_list=[]
        id_list=[]




        for post in L.get_hashtag_posts(HASHTAG):

            df = pd.DataFrame()
            post_likes = post.get_likes()
            post_comment = post.get_comments()
            profile_url = f"https://www.instagram.com/p/{post.shortcode}/"
            print(profile_url)
            # owner2 = f"https://www.instagram.com/{post.owner_username}/"
            profile_urls.append(profile_url)
            # url_post.append(post.display_url)
            print("list of users that liked the post")
           # with open('data20.csv', mode='a') as file:
            comment_list.clear()

            for comment in post_comment:
                    print(comment.owner.username)
                    comment_list.append(comment.owner.username)
            print(comment_list)

            for profile in post_likes:
                    ld += profile.username + ","
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

                    # my_object = {
                    #     "Url of Post": profile_url,
                    #     "Username": profile.username,
                    #     "Full Name": profile.full_name,
                    #     "Biography": profile.biography,
                    #     "Followers": profile.followers,
                    #     "Following": profile.followees,
                    #     "Number of Posts": profile.mediacount,
                    #     "Profile Picture URL": profile.profile_pic_url,
                    #     "Is Private": profile.is_private,
                    #     "Is Verified": profile.is_verified,
                    #     "has Liked": "True",
                    #     "has commented": bool(var1),
                    #     "description of Post": post.caption
                    # }
                   # my_object_string = json.dumps(my_object)
                    posturl_list.append(profile_url)
                    des_list.append(post.caption)
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


                    # Write the string to the CSV file
                    #file.write(my_object_string + '\n')

            #like_list.append(ld)
            # post_comment= post.get_comments()

            # Print the usernames of the profiles that liked the post
            # print("List of profiles that commented on the post:")
            # for comment in post_comment:
            # print(comment.owner.username)
            # comment_list.append(comment.owner.username)
        # id_list.append(count)
        # count = count + 1

        df = pd.DataFrame( {"URL": posturl_list, "description": des_list, "username": username_list, "fullname": fullname_list, "biography": biography_list, "followers": followers_list, "followers": followee_list, "Number of posts": np_list, "profile_pic_url": profile_pic_list, "is_private": isprivate_list, "is_verified": isverified_list,  "isliked": hasliked, "iscommented": hascommented})
        # df.drop_duplicates(subset="content", keep="first", inplace=True)
        df.to_csv("rent.csv")
        # df = pd.DataFrame({"url of the post": profile_urls,"List of people who liked the post": like_list,"List of people who comment on the post ": })
        # df.to_csv("output45.csv")

        #file.close()
        print("end time")
        print(time.time())
        url_list = []
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)