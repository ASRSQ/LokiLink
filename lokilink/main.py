from dataset import Dataset
from instancers import RandomUsersInstancer, RandomNewsInstancer, RandomPostInstancer
from news_sharing import ReachCalculator
from dataset_params import get_dataset_params

params = get_dataset_params()

total_users = params['total_users']
total_news = params['total_news']
total_posts = params['total_posts']
dataset_folder_path = params['dataset_folder_path']

dataset = Dataset(total_users, total_news, total_posts, dataset_folder_path)

user_instancer = RandomUsersInstancer(dataset)
news_instancer = RandomNewsInstancer(dataset)
post_instancer = RandomPostInstancer(dataset)
reach_calculator = ReachCalculator(dataset)
reach_calculator.calculate_reach_news_sharing()

dataset.generate_users_csv()
dataset.generate_posts_csv()
