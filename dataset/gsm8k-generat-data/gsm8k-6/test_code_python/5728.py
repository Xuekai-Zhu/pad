def solution():
    # Calculate the cost of one slice of cake
    cost_slice_cake = (3/4) * 2.4  # three-fourths of the cost of milk tea
    # Calculate the cost of 2 slices of cake
    cost_2_slices_cake = 2 * cost_slice_cake
    # Calculate the cost of 1 cup of milk tea
    cost_milk_tea = 2.4
    # Calculate the total cost of 2 slices of cake and 1 cup of milk tea
    total_cost = cost_2_slices_cake + cost_milk_tea
    result = total_cost
    return result

print(solution())