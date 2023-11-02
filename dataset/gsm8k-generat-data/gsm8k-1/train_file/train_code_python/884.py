def solution():
    """Bobby needs to buy a new pair of fancy shoes. He decides to go to a cobbler and get them handmade. 
    The cobbler charges $250 to make the mold. He then charges $75 an hour for 8 hours to make the shoes. 
    The cobbler agrees to only charge 80% of the cost for work to make the shoes, since it is his first pair of shoes. 
    How much did Bobby pay?"""
    mold_cost = 250
    hours_to_make_shoes = 8
    cost_per_hour = 75
    total_cost_of_work = hours_to_make_shoes * cost_per_hour
    cost_of_work_discounted = total_cost_of_work * .8
    total_cost = mold_cost + cost_of_work_discounted
    result = total_cost
    return result

print(solution())