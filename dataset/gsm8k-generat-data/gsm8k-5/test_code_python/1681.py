def solution():
    bottles_per_wash = 1/4 # Jake can wash his car 4 times with 1 bottle of car wash soap
    cost_per_bottle = 4.00 # Each bottle of car wash soap costs $4.00
    washes_per_week = 1 # Jake washes his car once a week
    weeks = 20 # Jake wants to know how much he will spend on car soap in 20 weeks

    # Calculate the total number of bottles of car wash soap Jake will need in 20 weeks
    total_bottles = bottles_per_wash * washes_per_week * weeks

    # Calculate the total cost of car wash soap Jake will spend in 20 weeks
    total_cost = total_bottles * cost_per_bottle
    result = total_cost
    return result

print(solution())