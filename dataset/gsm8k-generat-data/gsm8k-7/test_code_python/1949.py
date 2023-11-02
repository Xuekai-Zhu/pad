def solution():
    paintbrush_cost = 1.5
    paints_cost = 4.35
    easel_cost = 12.65
    current_money = 6.5

    # Calculate the total cost of all items
    total_cost = paintbrush_cost + paints_cost + easel_cost

    # Calculate how much more money Albert needs
    more_money_needed = total_cost - current_money
    result = more_money_needed
    return result

print(solution())