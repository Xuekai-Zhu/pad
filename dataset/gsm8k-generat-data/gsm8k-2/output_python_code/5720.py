def solution():
    """Chenny has 10 pieces of candies to be given out to her friends. She realized that she needs to buy 4 more so each of her friends will receive 2 candies. How many friends does Chenny have?"""
    candies = 10
    candies_per_friend = 2
    additional_candies = 4
    total_candies_needed = candies_per_friend * x
    total_candies = candies + additional_candies
    x = (total_candies - candies) // candies_per_friend
    result = x
    return result

print(solution())