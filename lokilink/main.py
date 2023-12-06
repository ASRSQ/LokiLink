import os
import numpy as np
import pandas as pd
from collections import deque
from dataset import Dataset
from instancers import RandomUsersInstancer, RandomNewsInstancer, RandomPostInstancer
from dataset_params import get_dataset_params

params = get_dataset_params()
total_users = params['total_users']
total_news = params['total_news']
total_posts = params['total_posts']

dataset = Dataset(total_users, total_news, total_posts)

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
