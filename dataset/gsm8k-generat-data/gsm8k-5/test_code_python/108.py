def solution():
    # Calculate the cost of the 4 pills that cost $1.50 each
    cost_of_four_pills = 4 * 1.5

    # Calculate the cost of the remaining pills
    cost_per_pill = 1.5 + 5.5  # The remaining pills are $5.50 more than the $1.50 pills
    remaining_pills = 9 - 4  # Henry takes a total of 9 pills a day, of which 4 pills cost $1.50 each
    cost_of_remaining_pills = remaining_pills * cost_per_pill

    # Calculate the total cost of the pills
    total_cost = (cost_of_four_pills + cost_of_remaining_pills) * 14  # Henry takes the pills for 14 days

    result = total_cost
    return result

print(solution())