def solution():
    amount_paid = 20  # John pays with a 20 dollar bill
    change_received = 14  # John gets 14 dollars in change
    total_cost = amount_paid - change_received  # John spent this much on 3 sodas

    # Calculate the cost per soda
    cost_per_soda = total_cost / 3
    result = cost_per_soda
    return result

print(solution())