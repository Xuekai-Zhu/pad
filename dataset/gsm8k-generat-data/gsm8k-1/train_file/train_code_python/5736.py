def solution():
    """Paula has 20 candies to be given out to her six friends. She needs to buy four additional candies so she can give an equal number of candies to her friends. How many candies will each of her friends get?"""
    total_candies = 24
    num_friends = 6
    candies_per_friend = total_candies // num_friends
    result = candies_per_friend
    return result

print(solution())