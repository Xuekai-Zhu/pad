def solution():
    cookies_per_chore = 3
    chores_per_week = 4
    total_chores = 2 * chores_per_week # Two siblings
    budget = 15
    pack_size = 24
    pack_cost = 3

    # Calculate the total number of cookies needed for each week
    total_cookies_per_week = total_chores * cookies_per_chore

    # Calculate the number of packs of cookies needed per week
    packs_per_week = total_cookies_per_week / pack_size
    packs_per_week = math.ceil(packs_per_week)

    # Calculate the cost of cookies per week
    cost_per_week = packs_per_week * pack_cost

    # Calculate the number of weeks Patty can go without doing chores
    weeks_without_chores = budget / cost_per_week
    result = math.floor(weeks_without_chores)
    return result

print(solution())