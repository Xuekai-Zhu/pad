def solution():
    initial_goldfish = 18
    goldfish_deaths = 5
    goldfish_purchased = 3
    total_weeks = 7
    goldfish_remaining = initial_goldfish - (total_weeks * goldfish_deaths) + (total_weeks * goldfish_purchased)
    result = goldfish_remaining
    return result

print(solution())