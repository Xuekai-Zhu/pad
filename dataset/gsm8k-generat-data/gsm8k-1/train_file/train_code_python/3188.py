def solution():
    """Gary buys 4 chickens. After two years, he has 8 times as many chickens as he started with. If each chicken lays 6 eggs a day, how many eggs does Gary currently collect every week?"""
    starting_chickens = 4
    final_chickens = starting_chickens * 8
    eggs_per_chicken = 6
    total_eggs_per_day = final_chickens * eggs_per_chicken
    total_eggs_per_week = total_eggs_per_day * 7
    result = total_eggs_per_week
    return result

print(solution())