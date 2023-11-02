def solution():
    """Tom plays an online trading card game. His deck has 19 rare cards, 11 uncommon, and 30 commons. The rare cards cost $1, the uncommon are $.50, and the commons are $.25 each. How much did his deck cost?"""
    rare_cards = 19
    uncommon_cards = 11
    common_cards = 30
    rare_cost = rare_cards * 1
    uncommon_cost = uncommon_cards * 0.5
    common_cost = common_cards * 0.25
    total_cost = rare_cost + uncommon_cost + common_cost
    result = total_cost
    return result

print(solution())