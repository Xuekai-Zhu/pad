def solution():
    initial_amount = 78
    cost_of_kite = 8
    cost_of_frisbee = 9

    # Calculate the total cost of the items Donny bought
    total_cost = cost_of_kite + cost_of_frisbee

    # Calculate the amount of money Donny has left
    amount_left = initial_amount - total_cost
    result = amount_left
    return result

print(solution())