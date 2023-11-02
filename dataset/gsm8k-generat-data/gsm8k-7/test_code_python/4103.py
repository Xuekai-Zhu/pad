def solution():
    budget = 60

    num_shower_gels = 4
    shower_gel_price = 4

    toothpaste_price = 3

    remaining_budget = 30

    # Calculate the total cost of all shower gels
    total_shower_gel_cost = num_shower_gels * shower_gel_price

    # Calculate the total cost of all items except laundry detergent
    total_without_detergent = total_shower_gel_cost + toothpaste_price

    # Calculate the cost of the laundry detergent
    detergent_cost = budget - remaining_budget - total_without_detergent

    result = detergent_cost
    return result

print(solution())