def solution():
    # Calculate the total cost of the items Anna bought
    gum_cost = 3 * 1.00
    chocolate_cost = 5 * 1.00
    candy_cane_cost = 2 * 0.50
    total_cost = gum_cost + chocolate_cost + candy_cane_cost

    # Calculate how much money Anna has left
    money_left = 10.00 - total_cost
    result = money_left
    return result

print(solution())