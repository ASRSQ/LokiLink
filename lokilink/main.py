import os
import numpy as np
import pandas as pd
import random
import uuid
from collections import deque

total_users = 100
total_news = 100
total_posts = 1000

df_users = pd.DataFrame(columns=['id', 'age', 'location', 'shared_news', 'posts_made', 'days_account_exists', 'posts_per_day', 'total_posts', 'fake_news_count', 'political_news_count', 'total_posts_reach', 'total_news_shared'])
df_posts = pd.DataFrame(columns=['id', 'source_idx', 'destination_idx', 'news_idx', 'is_fake_news', 'is_political_news'])

ages = [i for i in range(18, 65 + 1)]

cities = [
    'Ahch-To', 'Ando', 'Alderaan', 'Akiva', 'Asmeru', 'Bespin', 'Carida', 'Corellia', 'Coruscant',
    'Dagobah', 'Dantooine', 'Dathomir', 'Dorlo', 'Endor', 'Gentes', 'Geonosis', 'Hoth', 'Helska I',
    'Helska II', 'Helska III', 'Helska IV', 'Helska V', 'Helska VI', 'Helska VII', 'Jelucan', 'Kamino',
    'Kashyyyk', 'Kessel', 'Klatooine', 'Korriban', 'Krant', 'Kurat', 'Malachor', 'Mirial', 'Mustafar',
    'Mygeeto', 'Naboo', 'Neimoidia', 'Nova Plympto', 'Orto Plutonia', 'Plexis', 'Reyta', 'Rodia', 'Ruusan',
    'Ryloth', 'Scarif', 'Sembla', 'Serenno', 'Shili', 'Socorro', 'Tatooine', 'Utapau', 'Yavin', 'Zaloriis',
    'Zeitooine', 'Zygerria'
]

class AdjacencyMatrix:
  def __init__(self):
    self.mtx = [[0 for i in range(total_users)] for j in range(total_users)]
    self.reach_mtx = [[0 for i in range(total_users)] for j in range(total_users)]

  def addAdjacency(self, source, destination):
    self.mtx[source][destination] = 1

class News:
  def __init__(self, index=-1):
    self.id = index
    self.is_fake = random.choice([True, False])
    self.is_political = random.choice([True, False])
    self.am = AdjacencyMatrix()

  def toJson(self):
    return {
        'id': self.id,
        'is_fake': self.is_fake,
        'is_political': self.is_political
    }

class User:
  def __init__(self, index=-1):
    self.id = index
    self.shared_news = []
    self.posts_made = []
    self.age = random.randint(18, 65)
    self.location = random.choice(cities)

    self.days_account_exists = round(random.randint(1, 10 * 365))

    self.set_posts_per_day()
    self.total_posts = self.days_account_exists * self.posts_per_day

    self.total_posts_reach = 0 # alcance total (impressões do post)

    self.fake_news_count = 0
    self.political_news_count = 0
    self.total_news_shared = 0

  def set_posts_per_day(self):
    self.posts_per_day = round(random.randint(0, 1) + random.random(), 2)

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

def get_indexes_list_except(length, index):
    return [i for i in range(length) if i != index]

def get_random_index_except(length, index):
    indexes = get_indexes_list_except(length, index)
    random_index = random.choice(indexes)
    return random_index

def get_indexes_list(length):
    return [i for i in range(length)]

def get_random_index(length):
    indexes = get_indexes_list(length)
    return random.choice(indexes)

class Instancer:
  users = []
  news = []
  matrices = []

  def createUsers(self):
    for i in range(total_users):
      self.users.append(User(index=i))

    return self.users

  def createNews(self):
    for i in range(total_news):
      self.news.append(News(index=i))

    return self.news

instancer = Instancer()
news = instancer.createNews()
users = instancer.createUsers()

class ChanceBeingFriendsCalculator:
    def __init__(self, user):
      self.user = user

    def get_total_chance(self, friend):
        if self.user.id == friend.id:
          return 0

        chance_by_age = self.get_chance_by_age(friend)
        chance_by_location = self.get_chance_by_location(friend)
        change_by_randomness = random.random()
        return (2 * chance_by_age + 2 * chance_by_location + change_by_randomness) / 5

    def get_chance_by_age(self, friend):
        youngest_age = ages[0]
        oldest_age = ages[-1]

        age_difference = abs(self.user.age - friend.age)
        chance_being_friends = 1 - age_difference / (oldest_age - youngest_age)
        return round(chance_being_friends, 2)

    def get_chance_by_location(self, friend):
        location_a = cities.index(self.user.location)
        location_b = cities.index(friend.location)
        total_location = len(cities)

        location_difference = abs(location_a - location_b)
        chance_being_friends = 1 - location_difference / total_location
        return round(chance_being_friends, 2)

class FriendGenerator:
  def __init__(self, user):
    self.user = user
    self.chance_calculator = ChanceBeingFriendsCalculator(user)

  def get_random_friend(self):
    possible_friends = self.get_weighted_possible_friends_array()
    return random.choice(possible_friends)

  def get_weighted_possible_friends_array(self):
    weighted_possible_friends = []

    for i, possible_friend in enumerate(users):
      chance_being_friends = self.get_chance_of_being_friends(possible_friend)
      weight_being_friends = int(chance_being_friends * 100)
      weighted_possible_friend = [possible_friend for i in range(weight_being_friends)]
      weighted_possible_friends.extend(weighted_possible_friend)

    return weighted_possible_friends

  def get_chance_of_being_friends(self, friend):
      chance_being_friends = self.chance_calculator.get_total_chance(friend)
      return chance_being_friends

class RandomPost:
    def __init__(self, index=-1):
      self.id = index
      self.source_idx = get_random_index(total_users)

      source_user = users[self.source_idx]
      fg = FriendGenerator(source_user)

      destination_user = fg.get_random_friend()
      self.destination_idx = destination_user.id

      self.news_idx = get_random_index(total_news)
      self.news = news[self.news_idx]

    def toJson(self):
      return {
          'id': self.id,
          'source_idx': self.source_idx,
          'destination_idx': self.destination_idx,
          'news_idx': self.news_idx,
          'is_fake_news': self.news.is_fake,
          'is_political_news': self.news.is_political,
      }

class PostInstancer:
    posts = []

    def createPosts(self):
      for i in range(total_posts):
        self.posts.append(RandomPost(index=i))

      return self.posts

pi = PostInstancer()
posts = pi.createPosts()

for post in posts:
  source_idx = post.source_idx
  destination_idx = post.destination_idx
  post_news = post.news

  source_user = users[source_idx]

  source_user.add_post_made(post)
  source_user.add_shared_news(post_news)

  post_news.am.addAdjacency(source_idx, destination_idx)

def dfs_news(news_id):
  target_news = news[news_id]
  mtx = target_news.am.mtx
  transposed_mtx = np.transpose(mtx)
  reach = [0 for _ in range(total_users)]
  visited = set()

  def dfs_reach(user_id, distance):
    visited.add(user_id)
    reach[user_id] = distance

    for i, _ in enumerate(transposed_mtx[user_id]):
      if i not in visited and transposed_mtx[user_id][i] == 1:
        dfs_reach(i, distance + 1)

  for i in range(len(mtx)):
    if sum(mtx[i]) == 0:
        dfs_reach(i, 0)

  return reach

for i, current_news in enumerate(news):
  reach = dfs_news(i)

  for j, current_user in enumerate(users):
    current_user.total_posts_reach += reach[j]

for i, user in enumerate(users):
  df_users.loc[i] = user.toJson()

for i, post in enumerate(posts):
  df_posts.loc[i] = post.toJson()

dataset_path = './data'
os.makedirs(dataset_path, exist_ok=True)

df_users.to_csv(f'{dataset_path}/users.csv', index=False)
df_posts.to_csv(f'{dataset_path}/posts.csv', index=False)
