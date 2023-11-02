def solution():
    """Kaiden is collecting cans of soup for the local soup kitchen. He collects 158 cans during his first week and 259 during the second week. If his goal is to collect 500 cans how many more cans of soup does he need to collect?"""
    cans_collected = 158 + 259
    goal_cans = 500
    cans_needed = goal_cans - cans_collected
    result = cans_needed
    return result

print(solution())