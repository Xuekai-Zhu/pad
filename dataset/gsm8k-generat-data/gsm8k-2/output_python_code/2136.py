def solution():
    """In his garden, Grandpa had counted 36 small tomatoes before going on vacation. When he came back from vacation, he counted 100 times more tomatoes. How many tomatoes grew in his absence?"""
    starting_tomatoes = 36
    total_tomatoes = starting_tomatoes * 100
    tomatoes_grown = total_tomatoes - starting_tomatoes
    result = tomatoes_grown
    return result

print(solution())