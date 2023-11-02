def solution():
    nugs_per_box = 20  # There are 20 chicken nuggets in a box
    boxes_needed = 100/nugs_per_box  # Mark needs 5 boxes of chicken nuggets
    cost_per_box = 4  # Each box of chicken nuggets costs $4

    # Calculate the total cost for the chicken nuggets
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())