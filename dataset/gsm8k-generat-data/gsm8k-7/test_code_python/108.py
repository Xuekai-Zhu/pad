def solution():
    num_pills_per_day = 9
    num_days = 14
    cost_of_four_pills = 1.5

    # Calculate the total number of pills that Henry took in 14 days
    total_pills = num_pills_per_day * num_days

    # Calculate the number of pills that cost $5.50 more than the $1.50 pills
    num_expensive_pills = total_pills - 4

    # Calculate the total cost of the 4 $1.50 pills
    cost_of_four_pills_total = 4 * cost_of_four_pills

    # Calculate the total cost of the expensive pills
    cost_of_expensive_pills = num_expensive_pills * (cost_of_four_pills + 5.5)

    # Calculate the total cost of all the pills that Henry took
    total_cost = cost_of_four_pills_total + cost_of_expensive_pills
    result = total_cost
    return result

print(solution())