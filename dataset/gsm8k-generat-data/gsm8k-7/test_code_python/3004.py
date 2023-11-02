def solution():
    blueberry_cost = 5 / 6  # cost per ounce
    raspberry_cost = 3 / 8  # cost per ounce
    num_batches = 4
    fruit_per_batch = 12  # ounces

    # Calculate the total cost of using blueberries
    blueberry_total_cost = blueberry_cost * num_batches * fruit_per_batch

    # Calculate the total cost of using raspberries
    raspberry_total_cost = raspberry_cost * num_batches * fruit_per_batch

    # Calculate the difference in cost
    cost_difference = blueberry_total_cost - raspberry_total_cost
    result = cost_difference
    return result

print(solution())