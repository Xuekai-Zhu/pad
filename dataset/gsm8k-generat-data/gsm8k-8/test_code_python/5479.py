def solution():
    # Define the number of sets of drill bits and the cost per set
    num_sets = 5
    cost_per_set = 6

    # Calculate the subtotal before tax
    subtotal = num_sets * cost_per_set

    # Calculate the amount of tax
    tax_rate = 0.1
    tax_amount = tax_rate * subtotal

    # Calculate the total amount paid
    total_amount = subtotal + tax_amount
    result = total_amount
    return result

print(solution())