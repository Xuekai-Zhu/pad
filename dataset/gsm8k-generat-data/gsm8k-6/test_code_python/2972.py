def solution():
    # Assume the price of chair is x
    chair_price = float(input("Enter the price of chair: "))
    # Calculate the price of table
    table_price = 3 * chair_price 
    # Calculate the price of couch
    couch_price = 5 * table_price 
    # Calculate the total amount John paid for all items
    total_paid = chair_price + table_price + couch_price 
    # Find the price of the couch
    couch_price_paid = total_paid - chair_price - table_price
    result = couch_price_paid
    return result

print(solution())