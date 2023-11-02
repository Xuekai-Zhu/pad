def solution():
    num_barbells = 3
    total_paid = 850
    change = 40

    # Calculate the total cost of all barbells
    total_cost = total_paid - change

    # Calculate the cost of each barbell
    cost_per_barbell = total_cost / num_barbells
    result = cost_per_barbell
    return result

print(solution())