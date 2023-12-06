import random
from dataset_params import get_dataset_params

params = get_dataset_params()
cities = params['cities']
ages = params['ages']

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
  def __init__(self, user, users_list):
    self.user = user
    self.users_list = users_list
    self.chance_calculator = ChanceBeingFriendsCalculator(user)

  def get_random_friend(self):
    possible_friends = self.get_weighted_possible_friends_array()
    return random.choice(possible_friends)

  def get_weighted_possible_friends_array(self):
    weighted_possible_friends = []

    for i, possible_friend in enumerate(self.users_list):
      chance_being_friends = self.get_chance_of_being_friends(possible_friend)
      weight_being_friends = int(chance_being_friends * 100)
      weighted_possible_friend = [possible_friend for i in range(weight_being_friends)]
      weighted_possible_friends.extend(weighted_possible_friend)

    return weighted_possible_friends

  def get_chance_of_being_friends(self, friend):
      chance_being_friends = self.chance_calculator.get_total_chance(friend)
      return chance_being_friends
