def solution():
    """Josh had 100 gummy bear candies. He decided to give his 3 siblings 10 candies each. Then he gave half of the remaining candies to his best friend. If he only wants to eat 16 gummy bear candies, how many candies are left to be shared with others?"""
    total_candies = 100
    siblings_candies = 3 * 10
    remaining_candies = total_candies - siblings_candies
    friend_candies = remaining_candies / 2
    josh_candies = 16
    candies_left = remaining_candies - friend_candies - josh_candies
    result = candies_left
    return result

print(solution())