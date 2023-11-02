def solution():
    total_money = 10.0
    gum_cost = 1.0
    num_gum_packs = 3
    chocolate_cost = 1.0
    num_chocolates = 5
    candy_cane_cost = 0.5
    num_candy_canes = 2

    # Calculate the total cost of all candy items
    total_candy_cost = (gum_cost * num_gum_packs) + (chocolate_cost * num_chocolates) + (candy_cane_cost * num_candy_canes)

    # Calculate the amount of money Anna has left
    money_left = total_money - total_candy_cost
    result = money_left
    return result

print(solution())