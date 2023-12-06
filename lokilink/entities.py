import random

class AdjacencyMatrix:
  def __init__(self, size):
    self.size = size
    self.mtx = [[0 for i in range(size)] for j in range(size)]
    self.reach_mtx = [[0 for i in range(size)] for j in range(size)]

  def addAdjacency(self, source, destination):
    self.mtx[source][destination] = 1

class News:
  def __init__(self, index=-1):
    self.id = index
    self.is_fake = None
    self.is_political = None
    self.am = None

  def toJson(self):
    return {
        'id': self.id,
        'is_fake': self.is_fake,
        'is_political': self.is_political,
    }

class User:
  def __init__(self, index=-1):
    self.id = index
    self.shared_news = []
    self.posts_made = []
    self.age = None
    self.location = None

    self.days_account_exists = None
    self.posts_per_day = None
    self.total_posts = None

    self.total_posts_reach = 0
    self.fake_news_count = 0
    self.political_news_count = 0
    self.total_news_shared = 0

  def set_posts_per_day(self, posts_per_day):
    self.posts_per_day = posts_per_day
    self.update_total_posts()

  def set_days_account_exists(self, days_account_exists):
    self.days_account_exists = days_account_exists
    self.update_total_posts()

  def update_total_posts(self):
    if self.posts_per_day is None or self.days_account_exists is None:
      return

    self.total_posts = self.days_account_exists * self.posts_per_day

  def add_post_made(self, post):
    self.posts_made.append(post.id)

  def add_shared_news(self, target_news):
    if target_news.is_fake:
      self.fake_news_count += 1

    if target_news.is_political:
      self.political_news_count += 1

    news_idx = target_news.id
    self.total_news_shared += 1
    self.shared_news.append(news_idx)
    self.update_user_statistics()

  def update_user_statistics(self):
    self.fake_news_factor = round(self.fake_news_count / self.total_news_shared, 2)
    self.political_bias = round(self.political_news_count / self.total_news_shared, 2)

  def toJson(self):
    return {
        'id': self.id,
        'age': self.age,
        'location': self.location,
        'shared_news': [n for n in self.shared_news],
        'posts_made': [p for p in self.posts_made],
        'days_account_exists': self.days_account_exists,
        'posts_per_day': self.posts_per_day,
        'total_posts': self.total_posts,
        'fake_news_count': self.fake_news_count, 
        'political_news_count': self.political_news_count,
        'total_posts_reach': self.total_posts_reach,
        'total_news_shared': self.total_news_shared
    }

class Post:
    def __init__(self, index=-1):
      self.id = index
      self.source_idx = None
      self.source_user = None

      self.destination_idx = None
      self.destination_user = None
      
      self.news_idx = None
      self.news = None

    def set_source(self, source):
      self.source_idx = source.id
      self.source_user = source

    def set_destination(self, destination):
      self.destination_idx = destination.id
      self.destination_user = destination

    def set_news(self, news):
      self.news_idx = news.id
      self.news = news

    def toJson(self):
      return {
          'id': self.id,
          'source_idx': self.source_idx,
          'destination_idx': self.destination_idx,
          'news_idx': self.news_idx,
          'is_fake_news': self.news.is_fake,
          'is_political_news': self.news.is_political,
      }