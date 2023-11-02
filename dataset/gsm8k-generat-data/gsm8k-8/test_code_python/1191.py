def solution():
    # Define the initial cost and discount per bear
    initial_cost = 4.00
    discount_per_bear = 0.50

    # Calculate the cost for the first bear and total discount for the rest
    first_bear_cost = initial_cost
    rest_bears_discount = discount_per_bear * 100

    # Calculate the total cost for 101 bears
    total_cost = first_bear_cost + rest_bears_discount
    result = total_cost
    return result

print(solution())