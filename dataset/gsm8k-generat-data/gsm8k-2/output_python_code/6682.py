def solution():
    """There were 10 apples and 5 oranges in the basket. If Emily adds 5 more oranges to the basket, what percentage of the fruit in the basket would be apples?"""
    initial_apples = 10
    initial_oranges = 5
    new_oranges = 5
    total_fruit = initial_apples + initial_oranges + new_oranges
    apple_fraction = initial_apples / total_fruit
    apple_percentage = apple_fraction * 100
    result = apple_percentage
    return result

print(solution())