def solution():
    fraction_of_apple_per_day = 0.5      # Half of a small apple per day
    weight_of_small_apple = 0.25         # Small apple weighs 1/4 pound
    cost_per_pound = 2.0                 # Cost of apples is $2.00 per pound
    num_days = 14                        # Irene needs apples for 2 weeks (14 days)

    # Calculate the weight of apple required per day
    weight_of_apple_per_day = fraction_of_apple_per_day * weight_of_small_apple

    # Calculate the total weight of apple required for 2 weeks
    total_weight_of_apple = weight_of_apple_per_day * num_days

    # Calculate the total cost of all apples required
    total_cost = total_weight_of_apple * cost_per_pound
    result = total_cost
    return result

print(solution())