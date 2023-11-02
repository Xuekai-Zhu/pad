def solution():
    """Kaiden is collecting cans of soup for the local soup kitchen. He collects 158 cans during his first week and 259 during the second week. If his goal is to collect 500 cans how many more cans of soup does he need to collect?"""
    first_week_cans = 158
    second_week_cans = 259
    total_cans = first_week_cans + second_week_cans
    remaining_cans = 500 - total_cans
    result = remaining_cans
    return result

print(solution())