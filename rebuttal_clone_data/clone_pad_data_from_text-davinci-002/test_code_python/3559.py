def solution():
    loaves_of_bread = 3
    slices_per_loaf = 20
    bill_cost = 2 * 20
    change_received = 16
    total_slices = loaves_of_bread * slices_per_loaf
    cost_per_slice = (bill_cost - change_received) / total_slices
    result = cost_per_slice
    return result

print(solution())