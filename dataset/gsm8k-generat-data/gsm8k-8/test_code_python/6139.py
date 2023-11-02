def solution():
    # Define the cost of each item
    paintbrush_cost = 2.40
    paints_cost = 9.20
    easel_cost = 6.50

    # Define the amount of money Rose already has
    current_money = 7.10

    # Calculate the total cost of all items
    total_cost = paintbrush_cost + paints_cost + easel_cost

    # Calculate how much more money Rose needs
    more_money_needed = total_cost - current_money
    result = more_money_needed
    return result

print(solution())