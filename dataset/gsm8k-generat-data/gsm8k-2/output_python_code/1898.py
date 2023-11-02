def solution():
    """At the new store, there are 3 times as many grape candies as cherry candies, and 2 times as many apple candies as grape candies. All the candies cost $2.50 each. If the total cost of the candies is $200, how many grape candies does the store have?"""
    cherry_candies = x
    grape_candies = 3 * x
    apple_candies = 2 * grape_candies
    total_candies = cherry_candies + grape_candies + apple_candies
    total_cost = total_candies * 2.5
    grape_candies_cost = grape_candies * 2.5

    result = grape_candies
    return result

print(solution())