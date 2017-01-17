# このソフトウェアについて

GitHubリポジトリのプログラミング言語とByte数を取得しDBに挿入する。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* [GitHubアカウント](https://github.com/join?source=header-home)を作成する
* `repo`権限をもつ[AccessToken](https://github.com/settings/tokens)を作成する
* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)でGitHubアカウントDBを作成する
* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)でGitHubリポジトリDBを作成する
* [GiHub.Repo.Insert](https://github.com/ytyaru/GiHub.Repo.Insert.20170114155109609)で指定ユーザのリポジトリ情報をDBへ挿入する
* Main.pyにて以下の変数を設定する

```python
db_path_account = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'
db_path_repo = 'C:/GitHub.Repositories.{0}.sqlite3'.format(username)
```

# 実行

```dosbatch
python Main.py
```

# 結果

指定ユーザのGitHubリポジトリ情報が`GiHubApi.Repositories.{username}.sqlite3`ファイルの`Languages`テーブルに保存される。また、集計結果がコンソールに表示される。

![集計の例](https://cdn-ak.f.st-hatena.com/images/fotolife/y/ytyaru/20170117/20170117132535.png)

# 補足

TwoFactor認証アカウントは対象外。

今回は1リポジトリ1リクエスト必要。100リポジトリなら100リクエスト必要。
サーバ負荷を考慮して1リクエストあたり5～20秒待機している。
しかし、TwoFactor認証のOTPは30秒ごとに変わってしまう。
スクリプト実行完了までの間、絶えずWinAuthで取得し続けねばならない。
また、操作のわずかな間に無効なOTPでリクエストしてしまいかねない。
これらの理由から、TwoFactor認証アカウントは対象外とする。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
