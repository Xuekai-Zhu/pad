def solution():
    num_sets = 5
    set_cost = 6.0
    tax_rate = 0.1  # 10%

    # Calculate the total cost of all drill bit sets
    total_cost = num_sets * set_cost

    # Calculate the amount of tax
    tax = total_cost * tax_rate

    # Calculate the total amount paid, including tax
    total_paid = total_cost + tax
    result = total_paid
    return result

print(solution())