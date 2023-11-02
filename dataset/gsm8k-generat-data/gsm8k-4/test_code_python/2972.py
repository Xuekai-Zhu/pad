def solution():
    """John buys a chair. He then buys a table that is 3 times the price of the chair. Then, he buys a couch which is 5 times the price of the table. If John paid $380 for all these items, what is the price of the couch?"""
    # Define the price of the chair
    chair_price = x

    # Define the price of the table in terms of the chair
    table_price = 3 * chair_price

    # Define the price of the couch in terms of the table
    couch_price = 5 * table_price

    # Define the total cost of all items
    total_cost = 380

    # Define the equation for the total cost in terms of the chair
    # chair_price + table_price + couch_price = total_cost
    # Substituting table_price and couch_price in the above equation, and simplifying:
    19 * chair_price = 380
    chair_price = 20

    # Calculate the price of the couch in terms of the chair
    couch_price = 5 * table_price
    couch_price = 15 * chair_price

    result = couch_price
    return result

print(solution())