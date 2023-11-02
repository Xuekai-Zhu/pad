def solution():
    """It's Ava's birthday party. Her parents bought a unicorn piñata for $13 and filled it with all of her favorite treats. They bought 4 bags of Reese's for $9 per bag, 3 bags of Snickers for $5 per bag, and 5 bags of Skittles for $7 per bag. How much did the unicorn piñata and the treats cost altogether?"""
    unicorn_cost = 13
    reese_cost = 9
    snickers_cost = 5
    skittles_cost = 7
    total_treats_cost = (4 * reese_cost) + (3 * snickers_cost) + (5 * skittles_cost)
    total_cost = unicorn_cost + total_treats_cost
    result = total_cost
    return result

print(solution())