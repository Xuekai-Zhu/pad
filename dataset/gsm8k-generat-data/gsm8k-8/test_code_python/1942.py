def solution():
    #Define the cost of one pair of shorts
    cost_per_pair = 10

    #Calculate the cost of buying three pairs of shorts individually
    individual_cost = 3 * cost_per_pair

    #Calculate the discount for buying three pairs at once
    discount = 0.1

    #Calculate the total cost if Stacy buys three pairs at once
    total_cost_with_discount = (3 * cost_per_pair) * (1 - discount)

    #Calculate the amount saved by buying three pairs at once instead of individually
    amount_saved = individual_cost - total_cost_with_discount
    result = amount_saved
    return result

print(solution())