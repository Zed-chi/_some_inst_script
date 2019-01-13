from instabot import Bot
from dotenv import load_dotenv
import os
import re
from pprint import pprint


def get_taged_users(comment):
    user_regexp = re.compile(r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)")
    tagged_users = user_regexp.findall(comment)
    return list(filter(lambda user: is_user_exists(user), tagged_users))


def is_user_exists(name):
    return True if bot.get_user_id_from_username(name) else False


def get_valid_users(comments, likers, followers):
    users = []
    for comment in comments:
        id = comment['user_id']
        username = comment["user"]["username"]
        if str(id) not in likers and str(id) not in followers:
            continue
        if get_taged_users(comment["text"]):
            users.append((id, username))
    return users


if __name__ == "__main__":
    load_dotenv()
    login = os.getenv("login")
    passsword = os.getenv("pass")
    bot = Bot()
    bot.login(username=login, password=passsword)
    username = input("Введите имя аккаунта поста:")
    post_url = input("Введите ссылку на пост: ")
    if username and post_url:
        user_id = bot.get_user_id_from_username(username) \
            or exit("Неверное имя пользователя")
        post_id = bot.get_media_id_from_link(post_url) \
            or exit("Неверная ссылка на пост")
        likers = bot.get_media_likers(post_id)
        followers = bot.get_user_followers(user_id)
        comments = [x for x in bot.get_media_comments_all(post_id)]
        valid_users = get_valid_users(comments, likers, followers)
        names = set([user[1] for user in valid_users])
        pprint("Пользователи выполнившие условия:\n{}".format(names))
    else:
        print("Не введены данные")
