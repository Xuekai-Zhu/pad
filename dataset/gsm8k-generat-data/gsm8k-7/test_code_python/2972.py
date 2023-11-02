def solution():
    chair_price = x
    table_price = 3*x
    couch_price = 5*table_price
    total_cost = 380

    # Calculate the total cost of all items
    total_price = chair_price + table_price + couch_price

    # Calculate the price of the couch
    couch_price = total_cost - (chair_price + table_price)

    result = couch_price
    return result

print(solution())