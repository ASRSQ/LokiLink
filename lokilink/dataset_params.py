import argparse

arg_parser = argparse.ArgumentParser(description='Lonklink')

arg_parser.add_argument('--total-users', type=int, default=400, help='Total Quantity of Users')
arg_parser.add_argument('--total-news', type=int, default=200, help='Total Quantity of News')
arg_parser.add_argument('--total-posts', type=int, default=4000, help='Total Quantity of Posts')

arg_parser.add_argument('--weight-chance-age', type=float, default=2, help='Weight Chance Age')
arg_parser.add_argument('--weight-chance-location', type=float, default=2, help='Weight Chance Location')
arg_parser.add_argument('--weight-chance-randomness', type=float, default=1, help='Weight Chance Randomness')

arg_parser.add_argument('--max-age', type=int, default=65, help='Max Age')
arg_parser.add_argument('--min-age', type=int, default=18, help='Min Age')

cities = [
    'Ahch-To', 'Ando', 'Alderaan', 'Akiva', 'Asmeru', 'Bespin', 'Carida', 'Corellia', 'Coruscant',
    'Dagobah', 'Dantooine', 'Dathomir', 'Dorlo', 'Endor', 'Gentes', 'Geonosis', 'Hoth', 'Helska I',
    'Helska II', 'Helska III', 'Helska IV', 'Helska V', 'Helska VI', 'Helska VII', 'Jelucan', 'Kamino',
    'Kashyyyk', 'Kessel', 'Klatooine', 'Korriban', 'Krant', 'Kurat', 'Malachor', 'Mirial', 'Mustafar',
    'Mygeeto', 'Naboo', 'Neimoidia', 'Nova Plympto', 'Orto Plutonia', 'Plexis', 'Reyta', 'Rodia', 'Ruusan',
    'Ryloth', 'Scarif', 'Sembla', 'Serenno', 'Shili', 'Socorro', 'Tatooine', 'Utapau', 'Yavin', 'Zaloriis',
    'Zeitooine', 'Zygerria'
]

min_age = arg_parser.parse_args().min_age
max_age = arg_parser.parse_args().max_age
ages = [i for i in range(min_age, max_age + 1)]

def get_dataset_params():
    return {
        'total_users': arg_parser.parse_args().total_users,
        'total_news': arg_parser.parse_args().total_news,
        'total_posts': arg_parser.parse_args().total_posts,
        'weight_chance_age': arg_parser.parse_args().weight_chance_age,
        'weight_chance_location': arg_parser.parse_args().weight_chance_location,
        'weight_chance_randomness': arg_parser.parse_args().weight_chance_randomness,
        'max_age': arg_parser.parse_args().max_age,
        'min_age': arg_parser.parse_args().min_age,
        'ages': ages,
        'total_cities': len(cities),
        'cities': cities,
    }
