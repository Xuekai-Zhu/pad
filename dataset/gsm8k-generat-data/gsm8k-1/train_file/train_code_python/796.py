def solution():
    """Hannah has three dogs. The first dog eats 1.5 cups of dog food a day. The second dog eats twice as much while the third dog eats 2.5 cups more than the second dog. How many cups of dog food should Hannah prepare in a day for her three dogs?"""
    dog1 = 1.5
    dog2 = 2 * dog1
    dog3 = dog2 + 2.5
    total_food = dog1 + dog2 + dog3
    result = total_food
    return result

print(solution())