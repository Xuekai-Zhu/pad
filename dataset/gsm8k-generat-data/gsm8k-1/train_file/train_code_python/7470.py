def solution():
    """Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?"""
    children = 35
    chaperones = 5
    self = 1
    extra = 3
    total_people = children + chaperones + self + extra
    cost_per_lunch = 7
    total_cost = total_people * cost_per_lunch
    result = total_cost
    return result

print(solution())