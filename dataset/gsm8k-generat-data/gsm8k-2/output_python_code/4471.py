def solution():
    """Crackers contain 15 calories each and cookies contain 50 calories each. If Jimmy eats 7 cookies, how many crackers does he need to eat to have consumed a total of 500 calories?"""
    cookie_calories = 50
    cracker_calories = 15
    num_cookies = 7
    total_calories_from_cookies = cookie_calories * num_cookies
    remaining_calories_needed = 500 - total_calories_from_cookies
    num_crackers_needed = remaining_calories_needed // cracker_calories
    result = num_crackers_needed
    return result

print(solution())