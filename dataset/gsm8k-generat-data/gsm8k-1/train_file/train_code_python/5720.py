def solution():
    """Chenny has 10 pieces of candies to be given out to her friends. She realized that she needs to buy 4 more so each of her friends will receive 2 candies. How many friends does Chenny have?"""
    candies = 10
    candies_per_friend = 2
    extra_candies = 4
    total_candies_needed = candies_per_friend * (candies + extra_candies)
    friends = total_candies_needed / candies_per_friend
    result = friends
    return result

print(solution())