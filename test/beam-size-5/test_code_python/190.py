def solution():
    num_colors = 5
    color_price = 2
    prepared_amount = 20

    # Calculate the total cost of all crayons
    total_cost = num_colors * color_price

    # Calculate the amount of change
    change = prepared_amount - total_cost
    result = change
    return result

print(solution())