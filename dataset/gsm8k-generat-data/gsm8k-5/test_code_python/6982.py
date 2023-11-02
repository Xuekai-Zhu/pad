def solution():
    cost_per_half_pound = 0.6  # Half a pound of mangoes costs $0.60
    total_budget = 12  # Kelly has $12 to spend on mangoes

    # Calculate the number of half-pounds Kelly can buy with her total budget
    num_half_pounds = total_budget / cost_per_half_pound

    # Convert the number of half-pounds to pounds
    num_pounds = num_half_pounds / 2
    result = num_pounds
    return result

print(solution())