def solution():
    bottles_per_day = 0.5
    bottles_per_case = 24
    cost_per_case = 12.0
    num_days = 240

    # Calculate the total number of bottles of mineral water that Harper will drink
    total_bottles = num_days * bottles_per_day

    # Calculate the total number of cases of mineral water that Harper will need to buy
    total_cases = total_bottles / bottles_per_case

    # Calculate the total cost of all cases of mineral water that Harper will buy
    total_cost = total_cases * cost_per_case
    result = total_cost
    return result

print(solution())