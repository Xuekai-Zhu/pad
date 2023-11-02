def solution():
    cheapest_lamp_cost = 20
    most_expensive_lamp_cost = cheapest_lamp_cost * 3
    current_balance = 90

    # Calculate the cost of the most expensive lamp
    cost_of_lamp = most_expensive_lamp_cost

    # Calculate the remaining balance after buying the most expensive lamp
    remaining_balance = current_balance - cost_of_lamp
    result = remaining_balance
    return result

print(solution())