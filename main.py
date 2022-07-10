###############################
#THIS CODE IS A COMPLETE MESS
#HAB EUCH GEWARNT! 
#Um das Skript laufen zu lassen benötigt ihr den chrome webdriver von Selenium. Ich lade den mit hoch

from hashlib import new
import math
from attr import has
import pandas as pd
from psutil import users
from langdetect import detect
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import normalize

import numpy as np

arr =  []
i = 0
#Hier müsst ihr Natürlich den Ordner auswählen, in dem ihr alle Daten gespeichert habt.
while i < 1000:
    index = "D:\\Programming\\Python\\Web Scrawler\\toktok\\data\\1000_"+str(i)+".csv"
    arr.append(index)
    i +=1

#arrays
user = []
title = []
hashtags = []
music = []
likes = []
comments = []
shares = []
index = []
language = []

user_2 = []
title_2 = []
hashtags_2 = []
music_2 = []
likes_2 = []
comments_2 = []
shares_2 = []


ten_channels = []
ten_channels_count = []
top_ten_likes = []
least_ten_likes = []
ten_comments = []
ten_comments_users = []
ten_shares = []
ten_shares_users = []
ten_hashtags = []
ten_hashtags_count = []
ten_music = []
ten_music_count = []
distinct_music_count = []
ten_videos = []
ten_videos_count = []
ten_videos_index = []
ten_likes_index = []
ten_comments_index = []
ten_shares_index = []
#numbers

amount_100 = 0
amount_1000 = 0
amount_10000 = 0
amount_100000 = 0
amount_1000000 = 0
amount_10000000 = 0
amount_100000000 = 0

comments_100 = 0
comments_1000 = 0
comments_10000 = 0
comments_100000 = 0
comments_1000000 = 0
comments_10000000 = 0
comments_100000000 = 0

shares_100 = 0
shares_1000 = 0
shares_10000 = 0
shares_100000 = 0
shares_1000000 = 0
shares_10000000 = 0
shares_100000000 = 0

dataFrame = pd.concat(map(pd.read_csv, arr), ignore_index=True)
dataFrame.dropna()

def parse_number(num):
    new_num = 0
    dot = False
    null = 0
    if "." in num:
        for i in range(len(num)):
            if num[i].isnumeric():
                new_num += int(num[i])
            elif num[i] in ".":
                dot = True
            elif num[i] in "K":
                null = 100
            elif num[i] in "M":
                null = 100000
            if not dot:
                new_num = new_num * 10
        new_num = new_num * null
    else:
        for i in range(len(num)):
            if num[i].isnumeric():
                new_num += int(num[i])
            if not i == len(num) -1:
                new_num = new_num * 10
    return new_num
            
def parse_title(tit):
    hash = ""
    parsed_title = ""
    hash_array = []
    check_hash = False

    for char in tit:
        if char in "#":
            check_hash = True
            if len(hash) > 0:
                hash_array.append(hash)
                hash = ""
            hash += char
        elif char.isalpha():
            if check_hash:
                hash += char
            else:
                parsed_title += char
    title.append(parsed_title)
    hashtags.append(hash_array)
    #language.append(detect(str(parse_title)))


def parse_music(mus):
    if "Originalton" in mus:
        music.append("Originalton")
    elif "original sound" in mus:
        music.append("Originalton")
    else:
        music.append(mus)



# delete NaN rows and store values in arrays (with duplicates)
for i in range(len(dataFrame['User'])):
    check = False
    if type(dataFrame['User'][i]) == float:
        if math.isnan(dataFrame['User'][i]):
            check = True
    elif type(dataFrame['Hash'][i]) == float:
        if math.isnan(dataFrame['Hash'][i]):
            check = True
    elif type(dataFrame['Music'][i]) == float:
        if math.isnan(dataFrame['Music'][i]):
            check = True
    elif type(dataFrame['Likes'][i]) == float:
        if math.isnan(dataFrame['Likes'][i]):
            check = True
    elif type(dataFrame['Comments'][i]) == float:
        if math.isnan(dataFrame['Comments'][i]):
            check = True
    elif type(dataFrame['Shares'][i]) == float:
        if math.isnan(dataFrame['Shares'][i]):
            check = True
    if not check:
        user.append(dataFrame['User'][i])
        parse_title(dataFrame['Hash'][i])
        parse_music(dataFrame['Music'][i])
        likes.append(parse_number(dataFrame['Likes'][i]))
        comments.append(parse_number(dataFrame['Comments'][i]))
        shares.append(parse_number(dataFrame['Shares'][i]))

#eliminate duplicates
user_set = set([])
title_dict = {}
j = 0
for i in range(len(title)):
    if not title[i] in title_dict:
        title_dict[title[i]] = j
        index.append(j)
    j += 1
for i in index:
    user_2.append(user[i])
    hashtags_2.append(hashtags[i])
    title_2.append(title[i])
    music_2.append(music[i])
    likes_2.append(likes[i])
    comments_2.append(comments[i])
    shares_2.append(shares[i])
print("gesamt: " + str(len(dataFrame)))
print("brauchbar: " + str(len(title)))
print("ohne Duplikate: " + str(len(title_2)))
# Top 10 Users and amount they occurr (trend with duplicates)
top10_users_dict = {}
for i in user:
    if i in top10_users_dict:
        top10_users_dict[i] = top10_users_dict[i] + 1
    else: 
        top10_users_dict[i] = 1
#print(len(top10_users_dict))
mydict = dict(sorted(top10_users_dict.items(), key=lambda item: item[1],reverse=True))
for i in range(25):
    ten_channels.append(list(mydict.keys())[i])
    ten_channels_count.append(list(mydict.values())[i])

#amount of different users
different_users = len(top10_users_dict)
#print(different_users)
#print(ten_channels)
#print(ten_channels_count)

# Top 10 Videos and amount they occurr (trend with duplicates)
top10_videos_dict = {}
for i in title:
    if i in top10_videos_dict:
        top10_videos_dict[i] = top10_videos_dict[i] + 1
    else: 
        top10_videos_dict[i] = 1
video_dict = dict(sorted(top10_videos_dict.items(), key=lambda item: item[1],reverse=True))
for i in range(10):
    ten_videos.append(list(video_dict.keys())[i])
    ten_videos_count.append(list(video_dict.values())[i])
for i in ten_videos:
     ten_videos_index.append(title_2.index(i))

#different music
#print("music")
top10_music_dict = {}
for i in music_2:
    if i in top10_music_dict:
        top10_music_dict[i] = top10_music_dict[i] + 1
    else: 
        top10_music_dict[i] = 1
#print("music")
#print(len(top10_music_dict))
#print(len(music_2))
music_dit = dict(sorted(top10_music_dict.items(), key=lambda item: item[1],reverse=True))
for i in range(10):
    if i > 0:
        ten_music.append(list(music_dit.keys())[i])
        ten_music_count.append(list(music_dit.values())[i])
distinct_music_count = len(top10_music_dict)
#print(ten_music)
#print(ten_music_count)

#how often do videos occurr?
occur_dict = {}
for i in title:
    if i in occur_dict:
        occur_dict[i] = occur_dict[i] + 1
    else: 
        occur_dict[i] = 1
print(len(occur_dict))
count_occurr_dict = {}
count_occurr_dict["1"] = 0
count_occurr_dict["2"] = 0
count_occurr_dict["3"] = 0
count_occurr_dict["4"] = 0
count_occurr_dict["5"] = 0
count_occurr_dict["6"] = 0
count_occurr_dict["7"] = 0
count_occurr_dict["8"] = 0
count_occurr_dict["9"] = 0
count_occurr_dict["10"] = 0
count_occurr_dict["100"] = 0
count_occurr_dict["500"] = 0
count_occurr_dict["1000"] = 0
count_occurr_dict["2000"] = 0
count_occurr_dict["3000"] = 0
count_occurr_dict["4000"] = 0
count_occurr_dict2 = dict(sorted(occur_dict.items(), key=lambda item: item[1],reverse=True))
print("Wiederholungsrate")
for i in range(len(count_occurr_dict2)):
    if list(count_occurr_dict2.keys())[i] != "":
        if list(count_occurr_dict2.values())[i] == 1:
            count_occurr_dict["1"] = count_occurr_dict["1"] +1
        elif list(count_occurr_dict2.values())[i] == 2:
            count_occurr_dict["2"] = count_occurr_dict["2"] +1
        elif list(count_occurr_dict2.values())[i] == 3:
            count_occurr_dict["3"] = count_occurr_dict["3"] +1
        elif list(count_occurr_dict2.values())[i] == 4:
            count_occurr_dict["4"] = count_occurr_dict["4"] +1
        elif list(count_occurr_dict2.values())[i] == 5:
            count_occurr_dict["5"] = count_occurr_dict["5"] +1
        elif list(count_occurr_dict2.values())[i] == 6:
            count_occurr_dict["6"] = count_occurr_dict["6"] +1
        elif list(count_occurr_dict2.values())[i] == 7:
            count_occurr_dict["7"] = count_occurr_dict["7"] +1
        elif list(count_occurr_dict2.values())[i] == 8:
            count_occurr_dict["8"] = count_occurr_dict["8"] +1
        elif list(count_occurr_dict2.values())[i] == 9:
            count_occurr_dict["9"] = count_occurr_dict["9"] +1
        elif list(count_occurr_dict2.values())[i] == 10:
            count_occurr_dict["10"] = count_occurr_dict["10"] +1
        elif list(count_occurr_dict2.values())[i] <= 100:
            count_occurr_dict["100"] = count_occurr_dict["100"] +1
        elif list(count_occurr_dict2.values())[i] <= 500:
            count_occurr_dict["500"] = count_occurr_dict["500"] +1
        elif list(count_occurr_dict2.values())[i] <= 1000:
            count_occurr_dict["1000"] = count_occurr_dict["1000"] +1
        elif list(count_occurr_dict2.values())[i] <= 2000:
            count_occurr_dict["2000"] = count_occurr_dict["2000"] +1
        elif list(count_occurr_dict2.values())[i] <= 3000:
            count_occurr_dict["3000"] = count_occurr_dict["3000"] +1
        elif list(count_occurr_dict2.values())[i] <= 4000:
            count_occurr_dict["4000"] = count_occurr_dict["4000"] +1
print(count_occurr_dict)

#amount of likes based on comments
count_comment_dict = {}
count_comment_dict["100"] = 0
count_comment_dict["500"] = 0
count_comment_dict["1000"] = 0
count_comment_dict["2500"] = 0
count_comment_dict["5000"] = 0
count_comment_dict["7500"] = 0
count_comment_dict["10000"] = 0
count_comment_dict["15000"] = 0
count_comment_dict["20000"] = 0
count_comment_dict["30000"] = 0
count_comment_dict["50000"] = 0
count_comment_dict["100000"] = 0
index_comment100 = []
index_comment500 = []
index_comment1000 = []
index_comment2500 = []
index_comment5000 = []
index_comment7500 = []
index_comment10000 = []
index_comment15000 = []
index_comment20000 = []
index_comment30000 = []
index_comment50000 = []
index_comment100000 = []
like_amount_comment_100 = []
like_amount_comment_500 = []
like_amount_comment_1000 = []
like_amount_comment_2500 = []
like_amount_comment_5000 = []
like_amount_comment_7500 = []
like_amount_comment_10000 = []
like_amount_comment_15000 = []
like_amount_comment_20000 = []
like_amount_comment_30000 = []
like_amount_comment_50000 = []
like_amount_comment_100000 = []

print("Comments science")
for i in range(len(comments_2)):
    number_comment = comments_2[i]
    if number_comment <= 100:
        count_comment_dict["100"] = count_comment_dict["100"] +1
        index_comment100.append(i)
    elif number_comment <= 500:
        count_comment_dict["500"] = count_comment_dict["500"] +1
        index_comment500.append(i)
    elif number_comment <= 1000:
        count_comment_dict["1000"] = count_comment_dict["1000"] +1
        index_comment1000.append(i)
    elif number_comment <= 2500:
        count_comment_dict["2500"] = count_comment_dict["2500"] +1
        index_comment2500.append(i)
    elif number_comment <= 5000:
        index_comment5000.append(i)
        count_comment_dict["5000"] = count_comment_dict["5000"] +1
    elif number_comment <= 7500:
        index_comment7500.append(i)
        count_comment_dict["7500"] = count_comment_dict["7500"] +1
    elif number_comment <= 10000:
        index_comment10000.append(i)
        count_comment_dict["10000"] = count_comment_dict["10000"] +1
    elif number_comment <= 15000:
        index_comment15000.append(i)
        count_comment_dict["15000"] = count_comment_dict["15000"] +1
    elif number_comment <= 20000:
        index_comment20000.append(i)
        count_comment_dict["20000"] = count_comment_dict["20000"] +1
    elif number_comment <= 30000:
        index_comment30000.append(i)
        count_comment_dict["30000"] = count_comment_dict["30000"] +1
    elif number_comment <= 50000:
        index_comment50000.append(i)
        count_comment_dict["50000"] = count_comment_dict["50000"] +1
    else:
        index_comment100000.append(i)
        count_comment_dict["100000"] = count_comment_dict["100000"] +1
print(count_comment_dict)
for i in range(len(index_comment100)):
    like_amount_comment_100.append(likes_2[i])
for i in range(len(index_comment500)):
    like_amount_comment_500.append(likes_2[i])
for i in range(len(index_comment1000)):
    like_amount_comment_1000.append(likes_2[i])
for i in range(len(index_comment2500)):
    like_amount_comment_2500.append(likes_2[i])
for i in range(len(index_comment5000)):
    like_amount_comment_5000.append(likes_2[i])
for i in range(len(index_comment7500)):
    like_amount_comment_7500.append(likes_2[i])
for i in range(len(index_comment10000)):
    like_amount_comment_10000.append(likes_2[i])
for i in range(len(index_comment15000)):
    like_amount_comment_15000.append(likes_2[i])
for i in range(len(index_comment20000)):
    like_amount_comment_20000.append(likes_2[i])
for i in range(len(index_comment30000)):
    like_amount_comment_30000.append(likes_2[i])
for i in range(len(index_comment50000)):
    like_amount_comment_50000.append(likes_2[i])
for i in range(len(index_comment100000)):
    like_amount_comment_100000.append(likes_2[i])
blub_100 = 0
blub_500 = 0
blub_1000 = 0
blub_2500 = 0
blub_5000 = 0
blub_7500 = 0
blub_10000 = 0
blub_15000 = 0
blub_20000 = 0
blub_30000 = 0
blub_50000 = 0
blub_100000 = 0
for i in like_amount_comment_100:
    blub_100 += i
for i in like_amount_comment_500:
    blub_500 += i
for i in like_amount_comment_1000:
    blub_1000 += i
for i in like_amount_comment_2500:
    blub_2500 += i
for i in like_amount_comment_5000:
    blub_5000 += i
for i in like_amount_comment_7500:
    blub_7500 += i
for i in like_amount_comment_10000:
    blub_10000 += i
for i in like_amount_comment_15000:
    blub_15000 += i
for i in like_amount_comment_20000:
    blub_20000 += i
for i in like_amount_comment_30000:
    blub_30000 += i
for i in like_amount_comment_50000:
    blub_50000 += i
for i in like_amount_comment_100000:
    blub_100000 += i
print(blub_100/len(like_amount_comment_100), blub_500/len(like_amount_comment_500),blub_1000/len(like_amount_comment_1000), blub_2500/len(like_amount_comment_2500), blub_5000/len(like_amount_comment_5000), blub_7500/len(like_amount_comment_7500), blub_10000/len(like_amount_comment_10000), blub_15000/len(like_amount_comment_15000), blub_20000/len(like_amount_comment_20000), blub_30000/len(like_amount_comment_30000), blub_50000/len(like_amount_comment_50000), blub_100000/len(like_amount_comment_100000))

#Amount of likes based on shares
count_shares_dict = {}
count_shares_dict["100"] = 0
count_shares_dict["500"] = 0
count_shares_dict["1000"] = 0
count_shares_dict["2500"] = 0
count_shares_dict["5000"] = 0
count_shares_dict["7500"] = 0
count_shares_dict["10000"] = 0
count_shares_dict["15000"] = 0
count_shares_dict["20000"] = 0
count_shares_dict["30000"] = 0
count_shares_dict["50000"] = 0
count_shares_dict["100000"] = 0
index_share100 = []
index_share500 = []
index_share1000 = []
index_share2500 = []
index_share5000 = []
index_share7500 = []
index_share10000 = []
index_share15000 = []
index_share20000 = []
index_share30000 = []
index_share50000 = []
index_share100000 = []
like_amount_share_100 = []
like_amount_share_500 = []
like_amount_share_1000 = []
like_amount_share_2500 = []
like_amount_share_5000 = []
like_amount_share_7500 = []
like_amount_share_10000 = []
like_amount_share_15000 = []
like_amount_share_20000 = []
like_amount_share_30000 = []
like_amount_share_50000 = []
like_amount_share_100000 = []

print("Shares science")
for i in range(len(shares_2)):
    number_shares = shares_2[i]
    if number_shares <= 100:
        count_shares_dict["100"] = count_shares_dict["100"] +1
        index_share100.append(i)
    elif number_shares <= 500:
        count_shares_dict["500"] = count_shares_dict["500"] +1
        index_share500.append(i)
    if number_shares <= 1000:
        count_shares_dict["1000"] = count_shares_dict["1000"] +1
        index_share1000.append(i)
    elif number_shares <= 2500:
        count_shares_dict["2500"] = count_shares_dict["2500"] +1
        index_share2500.append(i)
    elif number_shares <= 5000:
        index_share5000.append(i)
        count_shares_dict["5000"] = count_shares_dict["5000"] +1
    elif number_shares <= 7500:
        index_share7500.append(i)
        count_shares_dict["7500"] = count_shares_dict["7500"] +1
    elif number_shares <= 10000:
        index_share10000.append(i)
        count_shares_dict["10000"] = count_shares_dict["10000"] +1
    elif number_shares <= 15000:
        index_share15000.append(i)
        count_shares_dict["15000"] = count_shares_dict["15000"] +1
    elif number_shares <= 20000:
        index_share20000.append(i)
        count_shares_dict["20000"] = count_shares_dict["20000"] +1
    elif number_shares <= 30000:
        index_share30000.append(i)
        count_shares_dict["30000"] = count_shares_dict["30000"] +1
    elif number_shares <= 50000:
        index_share50000.append(i)
        count_shares_dict["50000"] = count_shares_dict["50000"] +1
    elif number_shares > 50000:
        index_share100000.append(i)
        count_shares_dict["100000"] = count_shares_dict["100000"] +1
for i in range(len(index_share100)):
    like_amount_share_100.append(likes_2[i])
for i in range(len(index_share500)):
    like_amount_share_500.append(likes_2[i])
for i in range(len(index_share1000)):
    like_amount_share_1000.append(likes_2[i])
for i in range(len(index_share2500)):
    like_amount_share_2500.append(likes_2[i])
for i in range(len(index_share5000)):
    like_amount_share_5000.append(likes_2[i])
for i in range(len(index_share7500)):
    like_amount_share_7500.append(likes_2[i])
for i in range(len(index_share10000)):
    like_amount_share_10000.append(likes_2[i])
for i in range(len(index_share15000)):
    like_amount_share_15000.append(likes_2[i])
for i in range(len(index_share20000)):
    like_amount_share_20000.append(likes_2[i])
for i in range(len(index_share30000)):
    like_amount_share_30000.append(likes_2[i])
for i in range(len(index_share50000)):
    like_amount_share_50000.append(likes_2[i])
for i in range(len(index_share100000)):
    like_amount_share_100000.append(likes_2[i])
print(count_shares_dict)
blub_100_sh = 0
blub_500_sh = 0
blub_1000_sh = 0
blub_2500_sh = 0
blub_5000_sh = 0
blub_7500_sh = 0
blub_10000_sh = 0
blub_15000_sh = 0
blub_20000_sh = 0
blub_30000_sh = 0
blub_50000_sh = 0
blub_100000_sh = 0
for i in like_amount_share_100:
    blub_100_sh += i
for i in like_amount_share_500:
    blub_500_sh += i
for i in like_amount_share_1000:
    blub_1000_sh += i
for i in like_amount_share_2500:
    blub_2500_sh += i
for i in like_amount_share_5000:
    blub_5000_sh += i
for i in like_amount_share_7500:
    blub_7500_sh += i
for i in like_amount_share_10000:
    blub_10000_sh += i
for i in like_amount_share_15000:
    blub_15000_sh += i
for i in like_amount_share_20000:
    blub_20000_sh += i
for i in like_amount_share_30000:
    blub_30000_sh += i
for i in like_amount_share_50000:
    blub_50000_sh += i
for i in like_amount_share_100000:
    blub_100000_sh += i
print(blub_100_sh/len(like_amount_share_100), blub_500_sh/len(like_amount_share_500),blub_1000_sh/len(like_amount_share_1000), blub_2500_sh/len(like_amount_share_2500), blub_5000_sh/len(like_amount_share_5000), blub_7500_sh/len(like_amount_share_7500), blub_10000_sh/len(like_amount_share_10000), blub_15000_sh/len(like_amount_share_15000), blub_20000_sh/len(like_amount_share_20000), blub_30000_sh/len(like_amount_share_30000), blub_50000_sh/len(like_amount_share_50000), blub_100000_sh/len(like_amount_share_100000))
#different hashtags
#print("hashtags")
top10_hash_dict = {}
for i in hashtags:
    for j in i:
        if j in top10_hash_dict:
            top10_hash_dict[j] = top10_hash_dict[j] + 1
        else: 
            top10_hash_dict[j] = 1

hash_dit = dict(sorted(top10_hash_dict.items(), key=lambda item: item[1],reverse=True))
for i in range(10):
    ten_hashtags.append(list(hash_dit.keys())[i])
    ten_hashtags_count.append(list(hash_dit.values())[i])

#print(ten_hashtags)
#print(ten_hashtags_count)


#10 most liked Videos
sorted_likes_array = sorted(likes_2, reverse=True)
for i in range(10):
    top_ten_likes.append(sorted_likes_array[i])
    ten_likes_index.append(likes_2.index(sorted_likes_array[i]))

#print(top_ten_likes)

#10 least liked Videos
sorted_likes_array = sorted(likes_2)
for i in range(10):
    least_ten_likes.append(sorted_likes_array[i])

#print(least_ten_likes)

#number of videos with certain likes
for i in likes_2:
    if i <= 100:
        amount_100 += 1
    elif i <= 1000:
        amount_1000 += 1
    elif i <= 10000:
        amount_10000 += 1
    elif i <= 100000:
        amount_100000 += 1
    elif i <= 1000000:
        amount_1000000 += 1
    elif i <= 1000000:
        amount_1000000 += 1
    elif i <= 10000000:
        amount_10000000 += 1
    else:
        amount_100000000 += 1
for i in comments_2:
    if i <= 10:
        comments_100 += 1
    elif i <= 250:
        comments_1000 += 1
    elif i <= 500:
        comments_10000 += 1
    elif i <= 1000:
        comments_100000 += 1
    elif i <= 2500:
        comments_1000000 += 1
    elif i <= 5000:
        comments_10000000 += 1
    else:
        comments_100000000 += 1
for i in shares_2:
    if i <= 10:
        shares_100 += 1
    elif i <= 250:
        shares_1000 += 1
    elif i <= 500:
        shares_10000 += 1
    elif i <= 1000:
        shares_100000 += 1
    elif i <= 2500:
        shares_1000000 += 1
    elif i <= 5000:
        shares_10000000 += 1
    else:
        shares_100000000 += 1


#10 most shared Videos
sorted_shares_array = sorted(shares_2, reverse=True)
for i in range(10):
    ten_shares.append(sorted_shares_array[i])
    index = shares_2.index(sorted_shares_array[i])
    ten_shares_users.append(user_2[index])
    ten_shares_index.append(index)
#print(ten_shares)
#print(ten_shares_users)

#10 most commented Videos
sorted_comments_array = sorted(comments_2, reverse=True)
for i in range(10):
    ten_comments.append(sorted_comments_array[i])
    index = comments_2.index(sorted_comments_array[i])
    ten_comments_users.append(user_2[index])
    ten_comments_index.append(index)
#print(ten_comments)
#print(ten_comments_users)

############ CHARTS #####################
#Anzahl der Videos die die Top Lieder verwenden
data = {'Musik': ten_music,
        'Anzahl': ten_music_count
       }
df = pd.DataFrame(data,columns=['Musik','Anzahl'])
df.plot(x ='Musik', y='Anzahl', kind = 'bar')
plt.show()

#Anzahl die Top Hashtags verwenden
data = {'Hashtag': ten_hashtags,
        'Anzahl': ten_hashtags_count
       }
df = pd.DataFrame(data,columns=['Hashtag','Anzahl'])
df.plot(x ='Hashtag', y='Anzahl', kind = 'bar')
plt.show()

#data={'Likes': likes, 'Shares': shares, 'Comments': comments, 'Hashtags': hashtags, 'Music': music}

## grundlegende Statistiken
print("gesamte Videos:" + str(len(title)))
print("einzlende Videos:" + str(len(title_2)))
temp = [10, 7, 5, 4, 3, 2, 1]
data = {'Videos': temp,
        'Anzahl': [list(count_occurr_dict2.values())[6], list(count_occurr_dict2.values())[5], list(count_occurr_dict2.values())[4], list(count_occurr_dict2.values())[3], list(count_occurr_dict2.values())[2], list(count_occurr_dict2.values())[1], list(count_occurr_dict2.values())[0]]
       }
df = pd.DataFrame(data,columns=['Videos','Anzahl'])
df.plot(x ='Videos', y='Anzahl', kind = 'bar')
plt.show()
temp = [2000, 1500, 1000, 750, 500, 250]
data = {'Videos': temp,
        'Anzahl': [list(count_occurr_dict2.values())[6], list(count_occurr_dict2.values())[5], list(count_occurr_dict2.values())[4], list(count_occurr_dict2.values())[3], list(count_occurr_dict2.values())[2], list(count_occurr_dict2.values())[1]]
       }
df = pd.DataFrame(data,columns=['Videos','Anzahl'])
df.plot(x ='Videos', y='Anzahl', kind = 'bar')
plt.show()
print("Summe an likes, comments and shares")
lalalala = 0
for i in likes_2:
    lalalala += i
summe_likes = np.sum(likes_2)
summe_comments = np.sum(comments_2)
summe_shares = np.sum(shares_2)
print(lalalala, summe_likes, summe_comments, summe_shares)
print("Durchschnitt an likes, comments and shares")
summe_likes = np.mean(likes_2)
summe_comments = np.mean(comments_2)
summe_shares = np.mean(shares_2)
print(summe_likes, summe_comments, summe_shares)
print("Die Anzahl alle Musiktitel beträgt")
print(distinct_music_count)

## Was ist wichtiger? Likes, comments oder shares
print("Wiederholungszahlen aller Videos Likes")
print(amount_100)
print(amount_1000)
print(amount_10000)
print(amount_100000)
print(amount_1000000)
print(amount_10000000)
print(amount_100000000)
print("Wiederholungszahlen aller Videos comments")
print(comments_100)
print(comments_1000)
print(comments_10000)
print(comments_100000)
print(comments_1000000)
print(comments_10000000)
print(comments_100000000)
print("Wiederholungszahlen aller Videos shares")
print(shares_100)
print(shares_1000)
print(shares_10000)
print(shares_100000)
print(shares_1000000)
print(shares_10000000)
print(shares_100000000)
print("Gesamtanzahl an likes, comments and shares")
#corr Matrix
data = {'Likes': likes_2,
        'Comments': comments_2,
        'Shares': shares_2
        }
df = pd.DataFrame(data,columns=['Likes','Comments','Shares'])
corrMatrix = df.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()
#normalize 
n_likes = np.array(likes_2)
n_comments = np.array(comments_2)
n_shares = np.array(shares_2)
print(np.mean(normalize(n_likes[:,np.newaxis], axis=0)), np.mean(normalize(n_comments[:,np.newaxis], axis=0)), np.mean(normalize(n_shares[:,np.newaxis], axis=0)))

#relation between likes, comments and shares in different ranges
#ten most occured videos
sum_likes = 0
sum_comments = 0
sum_shares = 0
for i in ten_videos_index:
    sum_likes += likes_2[i]
    sum_comments += comments_2[i]
    sum_shares += shares_2[i]
print(sum_likes, sum_comments, sum_shares)
sum_all = sum_likes + sum_comments + sum_shares

labels = 'Likes', 'Comments', 'Shares'
sizes = [sum_likes/sum_all, sum_comments/sum_all, sum_shares/sum_all]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#ten most liked videos
sum_likes = 0
sum_comments = 0
sum_shares = 0
for i in ten_likes_index:
    sum_likes += likes_2[i]
    sum_comments += comments_2[i]
    sum_shares += shares_2[i]
print(sum_likes, sum_comments, sum_shares)
sum_all = sum_likes + sum_comments + sum_shares

labels = 'Likes', 'Comments', 'Shares'
sizes = [sum_likes/sum_all, sum_comments/sum_all, sum_shares/sum_all]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#ten most commented videos
sum_likes = 0
sum_comments = 0
sum_shares = 0
for i in ten_comments_index:
    sum_likes += likes_2[i]
    sum_comments += comments_2[i]
    sum_shares += shares_2[i]
print(sum_likes, sum_comments, sum_shares)
sum_all = sum_likes + sum_comments + sum_shares

labels = 'Likes', 'Comments', 'Shares'
sizes = [sum_likes/sum_all, sum_comments/sum_all, sum_shares/sum_all]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#ten most shared videos
sum_likes = 0
sum_comments = 0
sum_shares = 0
for i in ten_shares_index:
    sum_likes += likes_2[i]
    sum_comments += comments_2[i]
    sum_shares += shares_2[i]
print(sum_likes, sum_comments, sum_shares)
sum_all = sum_likes + sum_comments + sum_shares

labels = 'Likes', 'Comments', 'Shares'
sizes = [sum_likes/sum_all, sum_comments/sum_all, sum_shares/sum_all]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#have videos with more comments also more likes?


##Hashtags
trend_index = []
normal_index = []
mixed_index = []
empty_index = []
only_hash_index = []
hashtag_counter = 0
check_trend = False
check_normal = False
check_empty = False
for tags in hashtags_2:
    check_trend = False
    check_normal = False
    for i in tags:
        hashtag_empty = i in "#"
        check_la = i in "#fyp" or i in "#foryou" or i in "#viral" or i in "#fy" or i in "#foryourpage" or i in "#fürdich" or i in "trending" or i in "tiktok" or i in "goviral" or i in "trending" or i in "fypage"
        if check_la:
            if not check_trend:
                trend_index.append(hashtag_counter)
                check_trend = True
        elif not check_la and not hashtag_empty:
            if not check_normal:
                normal_index.append(hashtag_counter)
                check_normal = True
        elif hashtag_empty:
            if not check_empty:
                only_hash_index.append(hashtag_counter)
                check_empty = True
    if check_trend and check_normal:
        mixed_index.append(hashtag_counter)
    if len(tags) == 0:
        empty_index.append(hashtag_counter)
    hashtag_counter += 1
print(len(hashtags_2))
print(len(trend_index))
print(len(normal_index))
print(len(mixed_index))
print(len(only_hash_index))
print(len(empty_index))


#compare all 4 like numbers in total
sum_likes_trending = 0
sum_likes_normal = 0
sum_likes_mixed = 0
sum_likes_empty = 0
ten_trend = []
ten_normal = []
ten_mixed = []
ten_empty = []
ten_trend_video_index = []
ten_normal_video_index = []
ten_mixed_video_index = []
ten_empty_video_index = []
ten_trend_video = []
ten_normal_video = []
ten_mixed_video = []
ten_empty_video = []
for i in trend_index:
    sum_likes_trending += likes_2[i]
for i in normal_index:
    sum_likes_normal += likes_2[i]
for i in mixed_index:
    sum_likes_mixed += likes_2[i]
for i in empty_index:
    sum_likes_empty += likes_2[i]
labels = 'Trending', 'Normal', 'Mixed', 'Empty'
sizes = [sum_likes_trending, sum_likes_normal, sum_likes_mixed, sum_likes_empty]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#compare all 4 like numbers in mean
sum_all_labels = len(trend_index) + len(normal_index) + len(mixed_index) + len(empty_index)
labels = 'Trending', 'Normal', 'Mixed', 'Empty'
sizes = [sum_likes_trending/len(trend_index), sum_likes_normal/len(normal_index), sum_likes_mixed/len(mixed_index), sum_likes_empty/len(empty_index)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#10 most liked videos with trend hashtags
for i in trend_index:
    ten_trend.append(likes_2[i])
for i in normal_index:
    ten_normal.append(likes_2[i])
for i in mixed_index:
    ten_mixed.append(likes_2[i])
for i in empty_index:
    ten_empty.append(likes_2[i])

##
sumla1 = 0
sumla2 = 0
sumla3 = 0
sumla4 = 0
for i in ten_trend:
    sumla1 += i
for i in ten_normal:
    sumla2 += i
for i in ten_mixed:
    sumla3 += i
for i in ten_empty:
    sumla4 += i
print(sumla1, sumla2, sumla3, sumla4)
#

ten_trend = -np.sort(-np.array(ten_trend))
ten_normal = -np.sort(-np.array(ten_normal))
ten_mixed = -np.sort(-np.array(ten_mixed))
ten_empty = -np.sort(-np.array(ten_empty))
mean_trend = 0
mean_normal = 0
mean_mixed = 0
mean_empty = 0
for i in range(10):
    mean_trend += ten_trend[i]
    mean_normal += ten_normal[i]
    mean_mixed += ten_mixed[i]
    mean_empty += ten_empty[i]
print(mean_trend/10, mean_normal/10, mean_mixed/10, mean_empty/10)


for i in ten_trend:
    ten_trend_video_index.append(likes_2.index(i)) 
for i in ten_normal:
    ten_normal_video_index.append(likes_2.index(i))
for i in ten_mixed:
    ten_mixed_video_index.append(likes_2.index(i))
for i in ten_empty:
    ten_empty_video_index.append(likes_2.index(i))

for i in ten_trend_video_index:
    ten_trend_video.append(title_2[i])
for i in ten_normal_video_index:
    ten_normal_video.append(title_2[i])
for i in ten_mixed_video_index:
    ten_mixed_video.append(title_2[i])
for i in ten_trend_video_index:
    ten_empty_video.append(title_2[i])

for i in range(10):
    #print(ten_trend_video[i], ten_normal_video[i], ten_mixed_video[i], ten_empty_video[i])
    print(ten_trend_video[i])

##Music
print("Music")
sum_original = []
sum_other = []
for i in range(len(music_2)):
    if music_2[i] == "Originalton":
        sum_original.append(likes_2[i])
    else:
        sum_other.append(likes_2[i])
sum_la = 0
sum_lala = 0
for i in sum_original:
    sum_la += i
for i in sum_other:
    sum_lala += i
sum_la = sum_la/len(sum_original)
sum_lala = sum_la/len(sum_other)
sum_original = np.mean(np.array(sum_original))
sum_other = np.mean(np.array(sum_other))
print(sum_original, sum_other)
print("no py")
print(sum_la, sum_lala)

#likes from top10, 20, 30
likes_10 = []
likes_20 = []
likes_30 = []
likes_102 = []
likes_202 = []
likes_302 = []
top10_music = []
top20_music = []
top30_music = []
top10_music_score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
top20_music_score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
top30_music_score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(31):
    if i >= 0 and i < 10:
        likes_10.append(list(music_dit.keys())[i+1])
    elif i >= 10 and i < 20:
        likes_20.append(list(music_dit.keys())[i+1])
    elif i >= 20 and i < 30:
        likes_30.append(list(music_dit.keys())[i+1])

for i in range(len(music_2)):
    if music_2[i] in likes_10:
        likes_102.append(likes_2[i])
        top10_music.append(i)
    elif music_2[i] in likes_20:
        likes_202.append(likes_2[i])
        top20_music.append(i)
    elif music_2[i] in likes_30:
        likes_302.append(likes_2[i])
        top30_music.append(i)

#likes mean
print(np.mean(np.array(likes_102)), np.mean(np.array(likes_202)), np.mean(np.array(likes_302)))
labels = 'Top10', 'Top20', 'Top30'
sizes = [np.mean(np.array(likes_102)), np.mean(np.array(likes_202)), np.mean(np.array(likes_302))]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#likes sum
print(len(likes_102), len(likes_202), len(likes_302))
print(np.sum(np.array(likes_102)), np.sum(np.array(likes_202)), np.sum(np.array(likes_302)))
labels = 'Top10', 'Top20', 'Top30'
sizes = [np.sum(np.array(likes_102)), np.sum(np.array(likes_202)), np.sum(np.array(likes_302))]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() 

#check likes of top10 videos
#Die erste Person, die "tanzende Katzen" in die Kommentare schreibt, bekommt 10 Euro 
for i in top10_music:
    if likes_2[i] > min(top10_music_score):
        num = top10_music_score.index(min(top10_music_score))
        top10_music_score[num] = likes_2[i]
for i in top20_music:
    if likes_2[i] > min(top20_music_score):
        num = top20_music_score.index(min(top20_music_score))
        top20_music_score[num] = likes_2[i]
for i in top30_music:
    if likes_2[i] > min(top30_music_score):
        num = top30_music_score.index(min(top30_music_score))
        top30_music_score[num] = likes_2[i]

print(np.mean(np.array(top10_music_score)), np.mean(np.array(top20_music_score)), np.mean(np.array(top30_music_score)))
print(np.sum(np.array(top10_music_score)), np.sum(np.array(top20_music_score)), np.sum(np.array(top30_music_score)))
labels = 'Top10', 'Top20', 'Top30'
sizes = [np.sum(np.array(top10_music_score)), np.sum(np.array(top20_music_score)), np.sum(np.array(top30_music_score))]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() 

##Gender
##Categories
cat_sport = 0
cat_animal = 0
cat_beauty = 0
cat_life = 0
cat_gaming = 0
cat_it = 0
cat_motivation = 0
cat_food = 0
cat_anime = 0
cat_memes = 0
cat_asmr = 0
#Trends
elotrix = 0
monte = 0
ron = 0
inscope = 0
fernsehen = 0
trymacs = 0
for i in hashtags_2:
    for j in i:
        if j in "#sport" or j in "#fitness" or j in "#messi" or j in "#ronaldo" or j in "#football" or j in "#nfl" or j in "#NFL" or j in "#basketball":
            cat_sport += 1
        elif j in "#animal" or j in "#animals" or j in "#cat" or j in "#cats" or j in "#dog" or j in "#dogs":
            cat_animal += 1
        elif j in "#beauty" or j in "#makeup" or j in "#hair" or j in "#nails":
            cat_beauty += 1
        elif j in "#lifestyle" or j in "#life" or j in "#money" or j in "#adrenalin":
            cat_life += 1
        elif j in "#gaming" or j in "#minecraft" or j in "#fortnite" or j in "#cod" or j in "#twitch":
            cat_gaming += 1
        elif j in "#computer" or j in "#pc" or j in "#PC" or j in "#software" or j in "#hardware" or j in "#programming":
            cat_it += 1
        elif j in "#motivation":
            cat_motivation += 1
        elif j in "#food" or j in "#eating":
            cat_food += 1
        elif j in "#anime":
            cat_anime += 1
        elif j in "#memes" or j in "#dankmemes":
            cat_memes += 1
        elif j in "#asmr":
            cat_asmr += 1
        elif j in "#elotrix" or j in "#Elotrix":
            elotrix += 1
        elif j in "#monte" or j in "#montanablack" or j in "#Monte" or j in "#Montanablack":
            monte += 1
        elif j in "#ron" or j in "#tornado" or j in "#Tornado" or j in "#Ron" or j in "#ronbielecki":
            ron += 1
        elif j in "#inscope21" or j in "#inscope" or j in "#Inscope21" or j in "#Inscope":
            inscope += 1
        elif j in "#RTL" or j in "#rtl" or j in "#RTL2" or j in "#rtl2" or j in "#prosieben" or j in "#sat1":
            fernsehen += 1
        elif j in "#trymacs" or j in "#Trymacs":
            trymacs += 1
data = {'Kategorien': ["Sport", "Animals", "Beauty", "Life", "Gaming", "IT", "Motivation", "Food", "Anime", "Memes", "ASMR"],
        'Anzahl': [cat_sport, cat_animal, cat_beauty, cat_life, cat_gaming, cat_it, cat_motivation, cat_food, cat_anime, cat_memes, cat_asmr]
       }
df = pd.DataFrame(data,columns=['Kategorien','Anzahl'])
df.plot(x ='Kategorien', y='Anzahl', kind = 'bar')
plt.show()

##Bekannte Leute und Sender
data = {'Kategorien': ["Elotrix", "Monte", "Ron", "Inscope", "Fernsehen", "Trymacs"],
        'Anzahl': [elotrix, monte, ron, inscope, fernsehen, trymacs]
       }
df = pd.DataFrame(data,columns=['Kategorien','Anzahl'])
df.plot(x ='Kategorien', y='Anzahl', kind = 'bar')
plt.show()

#Top 10 Videos
top_ten_likes_videos = []
for i in ten_likes_index:
    top_ten_likes_videos.append(title_2[i])

# based on accurance    
print(ten_videos)
print(ten_videos_count)
#based on most likes
print(top_ten_likes_videos)
print(top_ten_likes)
#Top 10 Kanäle 
print(ten_channels)
print(ten_channels_count)