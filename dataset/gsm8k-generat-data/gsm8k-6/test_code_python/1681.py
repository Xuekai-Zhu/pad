def solution():
    # Calculate the total cost of car soap for 20 weeks
    cost_per_bottle = 4.00
    bottles_per_week = 1/4  # Jake can wash his car with 1 bottle of soap 4 times
    weeks = 20
    total_bottles = bottles_per_week * weeks
    total_cost = total_bottles * cost_per_bottle
    result = total_cost
    return result

print(solution())