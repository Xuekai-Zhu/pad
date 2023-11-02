def solution():
    # Calculate the total cost of Selena's meal
    steak_cost = 24 * 2
    burger_cost = 3.5 * 2
    ice_cream_cost = 2 * 3
    total_cost = steak_cost + burger_cost + ice_cream_cost

    # Calculate the amount of money Selena will be left with after her meal and tip
    amount_left = 99 - total_cost
    result = amount_left
    return result

print(solution())