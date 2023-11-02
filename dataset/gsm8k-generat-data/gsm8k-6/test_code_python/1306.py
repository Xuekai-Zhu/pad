def solution():
    # Calculate the total cost of Anna's candy purchases
    gum_cost = 3 * 1
    chocolate_cost = 5 * 1
    candy_cane_cost = 2 * 0.5
    total_cost = gum_cost + chocolate_cost + candy_cane_cost

    # Calculate how much money Anna has left
    money_left = 10 - total_cost
    result = money_left
    return result

print(solution())