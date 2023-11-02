def solution():
    # Cost of one stack of pancakes with bacon
    pancake_cost = 4
    bacon_cost = 2
    total_cost = pancake_cost + bacon_cost

    # Number of stacks of pancakes and slices of bacon sold
    pancake_stacks_sold = 60
    bacon_slices_sold = 90

    # Total amount raised
    total_raised = (pancake_cost * pancake_stacks_sold) + (bacon_cost * bacon_slices_sold)
    result = total_raised
    return result

print(solution())