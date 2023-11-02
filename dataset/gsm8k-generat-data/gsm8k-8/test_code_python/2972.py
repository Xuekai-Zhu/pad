def solution():
    # Let's assume the price of the chair is x
    x = 20

    # The price of the table is 3 times the price of the chair
    table_price = 3 * x

    # The price of the couch is 5 times the price of the table
    couch_price = 5 * table_price

    # Total price of all the items
    total_price = x + table_price + couch_price

    # John paid $380 for all items, so we solve for couch price
    couch_price = 380 - x - table_price

    result = couch_price
    return result

print(solution())