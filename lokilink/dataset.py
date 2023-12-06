import os
import pandas as pd

class Dataset:
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