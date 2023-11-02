def solution():
    # Let's assume the price of the chair as x
    chair_price = x

    # Table price is 3 times chair price
    table_price = 3 * chair_price

    # Couch price is 5 times table price
    couch_price = 5 * table_price

    # Total amount paid for all items is $380
    total_paid = 380

    # Equating the total paid amount with the sum of individual item's price
    # We get the equation below:
    x + 3*x + 5*3*x = 380

    # Simplifying the equation
    x = 20

    # Therefore, the price of the couch is 5 times the price of the table
    couch_price = 5 * table_price
    result = couch_price
    return result

print(solution())