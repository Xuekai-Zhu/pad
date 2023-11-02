def solution():
    """Josh had 100 gummy bear candies. He decided to give his 3 siblings 10 candies each. Then he gave half of the remaining candies to his best friend. If he only wants to eat 16 gummy bear candies, how many candies are left to be shared with others?"""
    total_candies = 100
    josh_siblings = 3
    candies_per_siblings = 10
    candies_given_to_siblings = josh_siblings * candies_per_siblings
    candies_remaining = total_candies - candies_given_to_siblings
    candies_given_to_friend = candies_remaining / 2
    josh_candies_remaining = candies_remaining - candies_given_to_friend - 16
    result = josh_candies_remaining
    return result

print(solution())