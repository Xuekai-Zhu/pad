def solution():
    toy_price = 20  # The price of a wooden toy is $20
    hat_price = 10  # The price of a hat is $10
    total_cost = (2 * toy_price) + (3 * hat_price)  # Kendra bought 2 toys and 3 hats
    change = 100 - total_cost  # Kendra paid with a $100 bill

    result = change
    return result

print(solution())