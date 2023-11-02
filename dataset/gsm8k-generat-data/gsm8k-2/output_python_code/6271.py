def solution():
    """There are 5 green candies, 3 blue candies, and 4 red candies in a bag. If Violet randomly picks a candy from the bag, how likely is it that it's blue?"""
    total_candies = 5 + 3 + 4
    blue_candies = 3
    probability = blue_candies / total_candies
    result = probability
    return result

print(solution())