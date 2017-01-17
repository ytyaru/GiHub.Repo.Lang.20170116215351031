#!python3
#encoding:utf-8

import requests
import json
import urllib.parse
from furl import furl

class Language:
    def __init__(self):
        pass
        self.username = None
        self.password = None
        self.otp = None
        self.token = None

    def set_account(self, username, password, otp=None):
        self.username = username
        self.password = password
        self.otp = otp
        self.token = None
        
    def set_token(self, token, otp=None):
        self.token = token
        self.otp = otp
        self.username = None
        self.password = None

    def get(self, username, repo_name):
        url = 'https://api.github.com/repos/{0}/{1}/languages'.format(username, repo_name)
        headers = self._get_http_headers(self.otp, self.token)
        if not(self.token is None):
            r = requests.get(url, headers=headers)
        elif not(self.username is None or self.password is None):
            r = requests.get(url, headers=headers, auth=(self.username, self.password))
        else:
            raise Exception('Account information is required.')
            return

        if not(200 == r.status_code):
            print(r.status_code)
            print(r.text)
            raise Exception('Failed request.')
            return None

        res = json.loads(r.text)
        """
        with open('GiHubApi.Repositories.Language.{0}.{1}.json'.format(username, repo_name), 'w') as f:
            f.write(r.text)
            print(r.text)
        """
        print(r.text)
        return res

    def _get_http_headers(self, otp=None, token=None):
        headers = {'Time-Zone': 'Asia/Tokyo',
                    'Content-Type': 'application/json; charset=utf-8'}
        if not(otp is None):
            headers['X-GitHub-OTP'] = otp
        if not(token is None):
            headers['Authorization'] = 'token {0}'.format(token)
        print(headers)
        return headers
