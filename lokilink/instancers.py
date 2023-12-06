import random
from utils import get_random_index
from entities import User, News, AdjacencyMatrix, Post
from news_sharing import FriendGenerator
from dataset_params import get_dataset_params

params = get_dataset_params()
cities = params['cities']
ages = params['ages']

class RandomUsersInstancer:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset_users = dataset.users
        self.create_users()

    def add_random_user(self):
        user = User()
        user.id = len(self._dataset_users)
        user.age = random.choice(ages)
        user.location = random.choice(cities)

        user.set_posts_per_day(round(random.randint(0, 1) + random.random(), 2))
        user.set_days_account_exists(round(random.randint(1, 10 * 365)))

        self._dataset_users.append(user)

        return user

    def create_users(self):
        for i in range(self._dataset.total_users):
            self.add_random_user()

        return self._dataset_users

class RandomNewsInstancer:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset_news = dataset.news
        self.create_news()

    def add_random_news(self):
        news = News()
        news.id = len(self._dataset_news)
        news.is_fake = random.choice([True, False])
        news.is_political = random.choice([True, False])
        news.am = AdjacencyMatrix(self._dataset.total_users)

        self._dataset_news.append(news)

        return news

    def create_news(self):
        for i in range(self._dataset.total_news):
            self.add_random_news()

        return self._dataset_news

class RandomPostInstancer:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset_news = dataset.news
        self._dataset_users = dataset.users
        self._dataset_posts = dataset.posts
        self.create_posts()

    def add_random_post(self):
        post = Post()
        post.id = len(self._dataset_posts)
        
        random_source = self.get_post_random_source()
        random_destination = self.get_post_random_destination(random_source)
        random_news = self.get_post_random_news()
        
        post.set_source(random_source)
        post.set_destination(random_destination)
        post.set_news(random_news)
        
        self.update_post_statistics(post)
        self._dataset_posts.append(post)

    def get_post_random_source(self):
        source_idx = get_random_index(self._dataset.total_users)
        source_user = self._dataset_users[source_idx]
        return source_user
    
    def get_post_random_destination(self, source_user):
        fg = FriendGenerator(source_user, self._dataset_users)
        destination_user = fg.get_random_friend()
        return destination_user

    def get_post_random_news(self):
        news_idx = get_random_index(self._dataset.total_news)
        selected_news = self._dataset_news[news_idx]
        return selected_news

    def update_post_statistics(self, post):
        post.source_user.add_post_made(post)
        post.source_user.add_shared_news(post.news)
        post.news.am.addAdjacency(post.source_idx, post.destination_idx)

    def create_posts(self):
        for i in range(self._dataset.total_posts):
            self.add_random_post()

        return self._dataset_posts
