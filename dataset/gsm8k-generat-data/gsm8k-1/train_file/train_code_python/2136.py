def solution():
    """In his garden, Grandpa had counted 36 small tomatoes before going on vacation. When he came back from vacation, he counted 100 times more tomatoes. How many tomatoes grew in his absence?"""
    initial_tomatoes = 36
    growth_factor = 100
    total_tomatoes = initial_tomatoes * growth_factor
    tomatoes_grown = total_tomatoes - initial_tomatoes
    result = tomatoes_grown
    return result

print(solution())