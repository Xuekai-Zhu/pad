def solution():
    # Calculate the total cost of buying 3 iPhones individually
    individual_cost = 3 * 600  

    # Calculate the total cost of buying 3 iPhones together with the discount
    discounted_cost = 0.95 * individual_cost  

    # Calculate the amount saved by buying together
    amount_saved = individual_cost - discounted_cost
    result = amount_saved
    return result

print(solution())