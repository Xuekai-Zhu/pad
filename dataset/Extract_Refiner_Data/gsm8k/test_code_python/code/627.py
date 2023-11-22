def solution():
    
    # Define the price of a diamond Jewell
    diamond_price = 2000

    # Calculate the price of a gold Jewell
    gold_price = (4/5) * diamond_price

    # Calculate the price of a silver Jewell
    silver_price = gold_price - 400

    # Calculate the total price for all three jewels
    total_price = diamond_price + gold_price + silver_price

    # Display the total price
    result = total_price
    return result

print(solution())