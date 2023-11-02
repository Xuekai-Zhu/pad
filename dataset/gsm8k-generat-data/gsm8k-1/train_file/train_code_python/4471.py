def solution():
    """Crackers contain 15 calories each and cookies contain 50 calories each. If Jimmy eats 7 cookies, how many crackers does he need to eat to have consumed a total of 500 calories?"""
    cookies_calories = 50
    crackers_calories = 15
    cookies_consumed = 7
    total_calories = 500
    remaining_calories = total_calories - (cookies_consumed * cookies_calories)
    crackers_needed = remaining_calories / crackers_calories
    result = crackers_needed
    return result

print(solution())