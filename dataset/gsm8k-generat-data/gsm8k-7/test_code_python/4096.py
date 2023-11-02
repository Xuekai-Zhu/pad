def solution():
    num_chickens = 3
    chicken_price = 3
    total_paid = 15

    # Calculate the total cost of all chickens
    total_chicken_cost = num_chickens * chicken_price

    # Calculate the cost of the potatoes
    potatoes_cost = total_paid - total_chicken_cost
    result = potatoes_cost
    return result

print(solution())