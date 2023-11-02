def solution():
    apple_pie_cost = 12  # Apple pie cost $12
    cheesecake_cost = (125 / 100) * apple_pie_cost  # One cheesecake is 25% cheaper than the apple pie
    muffins_cost = 2 * cheesecake_cost  # The six-pack of muffins is two times more expensive than one cheesecake

    # Calculate the total cost of the shopping
    total_cost = 2 * cheesecake_cost + apple_pie_cost + muffins_cost
    result = total_cost
    return result

print(solution())