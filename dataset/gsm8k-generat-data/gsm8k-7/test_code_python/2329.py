def solution():
    num_antibiotics_per_day = 3
    cost_per_antibiotic = 3
    num_days = 7

    # Calculate the total number of antibiotics needed for a week
    total_antibiotics = num_antibiotics_per_day * num_days

    # Calculate the total cost of all antibiotics needed for a week
    total_cost = total_antibiotics * cost_per_antibiotic
    result = total_cost
    return result

print(solution())