def solution():
    # Define the cost of each item
    paintbrush_cost = 1.5
    paint_set_cost = 4.35
    easel_cost = 12.65

    # Define Albert's starting balance
    starting_balance = 6.5

    # Calculate the total cost of all items
    total_cost = paintbrush_cost + paint_set_cost + easel_cost

    # Calculate how much more money Albert needs
    remaining_balance = total_cost - starting_balance
    result = remaining_balance
    return result

print(solution())