def solution():
    cheapest_lamp_cost = 20
    most_expensive_lamp_cost = 3 * cheapest_lamp_cost
    frank_current_money = 90

    # Calculate the cost of the most expensive lamp
    frank_spent_money = most_expensive_lamp_cost

    # Calculate how much money Frank has remaining
    frank_remaining_money = frank_current_money - frank_spent_money
    result = frank_remaining_money
    return result

print(solution())