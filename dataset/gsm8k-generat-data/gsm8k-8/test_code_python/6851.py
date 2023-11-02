def solution():
    # Define the cost of each type of glass
    small_glass_cost = 3
    large_glass_cost = 5

    # Define the number of small glasses purchased and the remaining amount of money
    num_small_glasses = 8
    remaining_money = 1

    # Calculate the total cost of the small glasses purchased
    total_small_glass_cost = num_small_glasses * small_glass_cost

    # Calculate the total amount of money spent on large glasses
    total_large_glass_cost = 50 - total_small_glass_cost - remaining_money

    # Calculate the number of large glasses purchased
    num_large_glasses = total_large_glass_cost / large_glass_cost

    result = num_large_glasses
    return result

print(solution())