def solution():
    """John buys a chair. He then buys a table that is 3 times the price of the chair. Then, he buys a couch that is 5 times the price of the table. If John paid $380 for all these items, what is the price of the couch?"""
    chair_price = x
    table_price = 3 * chair_price
    couch_price = 5 * table_price
    total_price = chair_price + table_price + couch_price
    if total_price == 380:
        result = couch_price
    else:
        result = "Solution not possible"
    return result

print(solution())