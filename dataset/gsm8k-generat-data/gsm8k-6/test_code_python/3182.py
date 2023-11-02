def solution():
    # Calculate the reduced price of a shirt and a leather jacket
    shirt_price = 60 - (0.20 * 60)
    jacket_price = 90 - (0.20 * 90)

    # Calculate the total cost of buying 5 shirts and 10 leather jackets at the reduced prices
    total_cost = (5 * shirt_price) + (10 * jacket_price)
    result = total_cost
    return result

print(solution())