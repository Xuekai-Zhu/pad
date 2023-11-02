def solution():
    num_loaves = 3
    slices_per_loaf = 20
    total_slices = num_loaves * slices_per_loaf
    total_paid = 40  # 2 x $20 bills
    change = 16

    # Calculate the total cost of all the slices of bread
    total_cost = total_paid - change

    # Calculate the cost per slice in cents
    cost_per_slice = (total_cost / total_slices) * 100
    result = cost_per_slice
    return result

print(solution())