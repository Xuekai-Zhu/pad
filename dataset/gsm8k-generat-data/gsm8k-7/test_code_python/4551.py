def solution():
    num_days = 22
    savings_per_day = 2
    flower_cost = 4
    
    # Calculate the total amount of savings that Lilly will have in 22 days
    total_savings = num_days * savings_per_day

    # Calculate the maximum number of flowers Lilly can buy with her savings
    num_flowers = total_savings // flower_cost
    result = num_flowers
    return result

print(solution())