def solution():
    """Selena got a tip today that amounted to $99. She pampered herself by eating at a 5-star hotel. She indulged herself with 2 steak meals that cost $24 each plate. She also ordered 2 types of burgers which cost $3.5 each, and 3 cups of ice cream which cost $2 each. How much money will Selena be left with?"""
    tip = 99
    steak_cost = 24
    burger_cost = 3.5
    ice_cream_cost = 2
    total_cost = 2 * steak_cost + 2 * burger_cost + 3 * ice_cream_cost
    money_left = tip - total_cost
    result = money_left
    return result

print(solution())