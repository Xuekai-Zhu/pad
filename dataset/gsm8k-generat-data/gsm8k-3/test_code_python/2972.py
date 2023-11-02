def solution():
    """John buys a chair. He then buys a table that is 3 times the price of the chair. Then, he buys a couch that is 5 times the price of the table. If John paid $380 for all these items, what is the price of the couch?"""
    # Define the price of the chair
    chair_price = x

    # Define the price of the table
    table_price = 3 * chair_price

    # Define the price of the couch
    couch_price = 5 * table_price

    # Calculate the total price of all the items
    total_price = chair_price + table_price + couch_price

    # Solve for the price of the couch
    couch_price = 380 - (chair_price + table_price)

    # Display the price of the couch
    result = couch_price
    return result

print(solution())