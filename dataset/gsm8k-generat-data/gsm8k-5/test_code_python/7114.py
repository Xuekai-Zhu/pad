def solution():
    money_paid = 850  # John pays $850
    change_received = 40  # John receives $40 in change
    num_barbells = 3  # John buys 3 barbells

    # Calculate the total cost of the barbells
    total_cost = money_paid - change_received
    cost_per_barbell = total_cost / num_barbells
    result = cost_per_barbell
    return result

print(solution())