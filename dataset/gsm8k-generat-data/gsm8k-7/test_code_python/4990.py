def solution():
    num_trousers = 10
    trousers_price = 9
    shirt_price = 5
    total_bill = 140

    # Calculate the total cost of all trousers
    total_trousers_cost = num_trousers * trousers_price

    # Calculate the cost of all shirts
    total_shirts_cost = total_bill - total_trousers_cost

    # Calculate the number of shirts
    num_shirts = total_shirts_cost / shirt_price

    # Calculate the number of missing shirts
    missing_shirts = 8 - num_shirts
    result = missing_shirts
    return result

print(solution())