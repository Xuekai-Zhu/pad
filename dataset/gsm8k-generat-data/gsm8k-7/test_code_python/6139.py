def solution():
    paintbrush_cost = 2.4
    paint_set_cost = 9.2
    easel_cost = 6.5
    current_money = 7.1

    # Calculate the total cost of all the supplies
    total_cost = paintbrush_cost + paint_set_cost + easel_cost

    # Calculate the amount of money Rose needs to buy all the supplies
    remaining_money = total_cost - current_money
    result = remaining_money
    return result

print(solution())