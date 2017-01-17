#!python3
#encoding:utf-8
import dataset
import time
import random
class Language:
    def __init__(self, db_path_repo):
        self.db_repo = dataset.connect('sqlite:///' + db_path_repo)

    """
    Insert programming language information for each GitHub repository into the database.
    @params [dict] langs is [List Languages](https://developer.github.com/v3/repos/#list-languages) Response.
    """
    def insert(self, repo_id, langs):
        for lang in langs.keys():
            self.db_repo['Languages'].insert(dict(
                RepositoryId=repo_id,
                Language=lang,
                Size=langs[lang]))
            print("{0},{1},{2}".format(repo_id, lang, langs[lang]))
