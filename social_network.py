# social_network.py
import json
from datetime import datetime

class User:
    def __init__(self, username, name):
        self.username = username
        self.name = name
        self.followers = []
        self.following = []
        self.posts = []

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now()
        self.likes = []
        self.comments = []

    def like(self, user):
        if user not in self.likes:
            self.likes.append(user)

    def add_comment(self, user, content):
        comment = Comment(user, content)
        self.comments.append(comment)
        return comment

class Comment:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now()

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.posts = []

    def create_user(self, username, name):
        if username not in self.users:
            user = User(username, name)
            self.users[username] = user
            return user
        return None

    def get_user(self, username):
        return self.users.get(username)

    def create_post(self, username, content):
        user = self.get_user(username)
        if user:
            post = user.create_post(content)
            self.posts.append(post)
            return post
        return None

    def get_user_posts(self, username):
        user = self.get_user(username)
        return user.posts if user else []

    def get_feed(self, username):
        user = self.get_user(username)
        if not user:
            return []
        feed = []
        for followed_user in user.following:
            feed.extend(followed_user.posts)
        feed.extend(user.posts)
        feed.sort(key=lambda x: x.timestamp, reverse=True)
        return feed

    def save_to_json(self, filename):
        data = {
            "users": {},
            "posts": []
        }
        
        # Guardar usuarios
        for username, user in self.users.items():
            data["users"][username] = {
                "name": user.name,
                "followers": [u.username for u in user.followers],
                "following": [u.username for u in user.following]
            }
        
        # Guardar posts
        for post in self.posts:
            post_data = {
                "author": post.author.username,
                "content": post.content,
                "timestamp": post.timestamp.isoformat(),
                "likes": [u.username for u in post.likes],
                "comments": [{
                    "author": comment.author.username,
                    "content": comment.content,
                    "timestamp": comment.timestamp.isoformat()
                } for comment in post.comments]
            }
            data["posts"].append(post_data)
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)