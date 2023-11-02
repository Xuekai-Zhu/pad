def solution():
    """At the new store, there are 3 times as many grape candies as cherry candies, and 2 times as many apple candies as grape candies.
    All the candies cost $2.50 each. If the total cost of the candies is $200, how many grape candies does the store have?"""
    cost_per_candy = 2.5
    total_cost = 200
    cherry_candies = 1
    grape_candies = 3 * cherry_candies
    apple_candies = 2 * grape_candies
    
    total_candies = cherry_candies + grape_candies + apple_candies
    grape_cost = grape_candies * cost_per_candy
    grape_percentage = grape_cost / total_cost
    
    result = grape_candies

    return result

print(solution())