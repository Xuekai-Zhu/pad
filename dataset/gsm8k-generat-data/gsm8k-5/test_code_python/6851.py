def solution():
    small_glass_cost = 3
    large_glass_cost = 5
    total_budget = 50
    small_glasses_bought = 8
    change_left = 1

    # Calculate the total cost of the small glasses bought
    small_glasses_cost = small_glass_cost * small_glasses_bought

    # Calculate the remaining budget after buying the small glasses
    remaining_budget = total_budget - small_glasses_cost

    # Calculate the maximum number of large glasses Peter can buy with the remaining budget
    max_large_glasses = remaining_budget // large_glass_cost

    # Calculate the number of large glasses Peter actually bought
    large_glasses_bought = max_large_glasses - (remaining_budget % large_glass_cost == change_left)

    result = large_glasses_bought
    return result

print(solution())