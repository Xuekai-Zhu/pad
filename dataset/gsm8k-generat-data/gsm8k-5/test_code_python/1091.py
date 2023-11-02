def solution():
    bottles_per_day = 1/2  # Harper drinks 1/2 bottle of mineral water per day
    bottles_per_case = 24  # There are 24 bottles of mineral water in a case
    days = 240  # Harper wants the mineral water to last for 240 days

    # Calculate the total number of bottles Harper needs
    total_bottles = bottles_per_day * days

    # Calculate the total number of cases Harper needs
    total_cases = total_bottles / bottles_per_case

    # Calculate the total cost of the mineral water
    cost_per_case = 12.00  # The cases are on sale for $12.00 each
    total_cost = total_cases * cost_per_case
    result = total_cost
    return result

print(solution())