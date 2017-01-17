#!python3
#encoding:utf-8

import os
from pathlib import Path
from github import Language as HubLang
from sqlite import Language as SqlLang
from datetime import datetime
import json
import dataset
import random
import time

db_path_account = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'
username = 'ytyaru'
db_path_repo = 'C:/GitHub.Repositories.{0}.sqlite3'.format(username)

# --------------------------------------
# 取得＆挿入
# --------------------------------------
db_account = dataset.connect('sqlite:///' + db_path_account)
db_repo = dataset.connect('sqlite:///' + db_path_repo)

hub_lang = HubLang.Language()
sql_lang = SqlLang.Language(db_path_repo)

account = db_account['Accounts'].find_one(Username=username)
hub_lang.set_token(db_account['AccessTokens'].find_one(AccountId=account['Id'])['AccessToken'])

for repo in db_repo['Repositories'].find(order_by='CreatedAt'):
    lang = db_repo['Languages'].find_one(RepositoryId=repo['Id'])
    if not(lang is None):
        continue
    
    sql_lang.insert(repo['Id'], hub_lang.get(username, repo['Name']))
    
    sleep_time = 5 + random.randint(0,15)
    time.sleep(sleep_time)

# --------------------------------------
# 集計
# --------------------------------------
for res in db_repo.query('select min(CreatedAt) FirstDate from Repositories'):
    print('FirstDate: {0}'.format(res['FirstDate']))
for res in db_repo.query('select max(CreatedAt) LastDate from Repositories'):
    print('LastDate:  {0}'.format(res['LastDate']))

print("all repos: {0}".format(db_repo['Repositories'].count()))
for res in db_repo.query('select sum(Size) AllSize from Languages'):
    print('all size:  {0} Byte'.format(res['AllSize']))

# 桁あわせ：最も長い言語名を取得する
name_length = 0
for res in db_repo.query('select * from Languages where length(Language)=(select max(length(Language)) from Languages)'):
    name_length = res['Language']

# 桁あわせ：最も大きい言語別合計Byteを取得する
size_length = db_repo.query('select sum(Size) SumSize from Languages group by Language order by SumSize desc').next()['SumSize']

# 言語別の合計Byte数
format_str = "  {0:<%d}: {1:>%d} Byte" % (len(name_length), len(str(size_length)))
for lang in db_repo.query('select Language, sum(Size) SumSize from Languages group by Language order by SumSize desc'):
    print(format_str.format(lang['Language'], lang['SumSize']))
