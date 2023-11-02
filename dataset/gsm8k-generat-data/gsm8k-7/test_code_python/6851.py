def solution():
    small_glass_cost = 3
    large_glass_cost = 5
    total_budget = 50
    num_small_glasses = 8
    change = 1

    # Calculate the total cost of small glasses
    total_small_glasses_cost = num_small_glasses * small_glass_cost

    # Calculate the amount spent on large glasses
    amount_spent_on_large_glasses = total_budget - total_small_glasses_cost - change

    # Calculate the number of large glasses bought with the remaining budget
    num_large_glasses = amount_spent_on_large_glasses // large_glass_cost
    result = num_large_glasses
    return result

print(solution())