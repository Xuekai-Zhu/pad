def solution():
    first_bear_price = 4.0
    discount_per_bear = 0.5
    num_bears = 101

    # Calculate the cost of the first bear
    total_cost = first_bear_price

    # Calculate the cost of the remaining bears with discount
    for i in range(2, num_bears + 1):
        total_cost += first_bear_price - (discount_per_bear * (i - 1))

    result = total_cost
    return result

print(solution())