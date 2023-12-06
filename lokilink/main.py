import os
import numpy as np
import pandas as pd
import uuid
from collections import deque
from instancers import RandomUsersInstancer, RandomNewsInstancer, RandomPostInstancer

class DatasetGenerator:
    def __init__(self, total_users, total_news, total_posts):
        self.total_users = total_users
        self.total_news = total_news
        self.total_posts = total_posts
        self.users = []
        self.news = []
        self.posts = []
        self.dataset_folder_path = 'data'

    def generate_users_csv(self):
        df_users = pd.DataFrame(columns=['id', 'age', 'location', 'shared_news', 'posts_made', 'days_account_exists', 'posts_per_day', 'total_posts', 'fake_news_count', 'political_news_count', 'total_posts_reach', 'total_news_shared'])
        
        for i, user in enumerate(self.users):
            df_users.loc[i] = user.toJson()

        os.makedirs(self.dataset_folder_path, exist_ok=True)
        df_users.to_csv(f'{self.dataset_folder_path}/users.csv', index=False)

    def generate_posts_csv(self):
        df_posts = pd.DataFrame(columns=['id', 'source_idx', 'destination_idx', 'news_idx', 'is_fake_news', 'is_political_news'])

        for i, post in enumerate(self.posts):
            df_posts.loc[i] = post.toJson()

        os.makedirs(self.dataset_folder_path, exist_ok=True)
        df_posts.to_csv(f'{self.dataset_folder_path}/posts.csv', index=False)


dataset = DatasetGenerator(400, 200, 4000)
user_instancer = RandomUsersInstancer(dataset)
news_instancer = RandomNewsInstancer(dataset)
post_instancer = RandomPostInstancer(dataset)

dataset.generate_users_csv()
dataset.generate_posts_csv()

print(dataset.posts)

# for post in posts:
#   source_idx = post.source_idx
#   destination_idx = post.destination_idx
#   post_news = post.news

#   source_user = users[source_idx]

#   source_user.add_post_made(post)
#   source_user.add_shared_news(post_news)

#   post_news.am.addAdjacency(source_idx, destination_idx)

# def dfs_news(news_id):
#   target_news = news[news_id]
#   mtx = target_news.am.mtx
#   transposed_mtx = np.transpose(mtx)
#   reach = [0 for _ in range(total_users)]
#   visited = set()

#   def dfs_reach(user_id, distance):
#     visited.add(user_id)
#     reach[user_id] = distance

#     for i, _ in enumerate(transposed_mtx[user_id]):
#       if i not in visited and transposed_mtx[user_id][i] == 1:
#         dfs_reach(i, distance + 1)

#   for i in range(len(mtx)):
#     if sum(mtx[i]) == 0:
#         dfs_reach(i, 0)

#   return reach

# for i, current_news in enumerate(news):
#   reach = dfs_news(i)

#   for j, current_user in enumerate(users):
#     current_user.total_posts_reach += reach[j]

# for i, user in enumerate(users):
#   df_users.loc[i] = user.toJson()



# dataset_path = './data'
# os.makedirs(dataset_path, exist_ok=True)

# df_users.to_csv(f'{dataset_path}/users.csv', index=False)
