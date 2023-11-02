def solution():
    """Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?"""
    total_people = 35 + 5 + 1 + 3
    cost_per_lunch = 7
    total_lunches = total_people * 1.03
    total_cost = total_lunches * cost_per_lunch
    result = total_cost
    return result

print(solution())