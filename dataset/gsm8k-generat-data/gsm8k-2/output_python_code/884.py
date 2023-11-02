def solution():
    """Bobby needs to buy a new pair of fancy shoes. He decides to go to a cobbler and get them handmade. The cobbler charges $250 to make the mold. He then charges $75 an hour for 8 hours to make the shoes. The cobbler agrees to only charge 80% of the cost for work to make the shoes, since it is his first pair of shoes. How much did Bobby pay?"""
    mold_cost = 250
    shoes_time = 8
    shoes_cost = 75 * shoes_time
    total_cost = mold_cost + (0.8 * shoes_cost)
    result = total_cost
    return result

print(solution())