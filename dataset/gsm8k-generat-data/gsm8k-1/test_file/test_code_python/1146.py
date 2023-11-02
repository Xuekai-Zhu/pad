def solution():
    """Patricia has 30 roses. She gave 24 roses to her mother. She bought 15 more roses. How many roses did she have now?"""
    initial_roses = 30
    roses_given_away = 24
    roses_bought = 15
    total_roses = initial_roses - roses_given_away + roses_bought
    result = total_roses
    return result

print(solution())