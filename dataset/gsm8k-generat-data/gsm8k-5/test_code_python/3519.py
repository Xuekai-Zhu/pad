def solution():
    cost_per_box = 7.50  # A box of ice cream bars costs $7.50
    bars_per_box = 3  # A box of ice cream bars contains three bars
    friends = 6  # Six friends want to each eat 2 bars

    # Calculate the number of boxes needed
    boxes_needed = (2 * friends) / bars_per_box

    # Calculate the total cost
    total_cost = boxes_needed * cost_per_box

    # Calculate the cost per person
    cost_per_person = total_cost / friends / 2
    result = cost_per_person
    return result

print(solution())