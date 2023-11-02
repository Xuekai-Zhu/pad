def solution():
    """Du Chin bakes 200 meat pies in a day. He sells them for $20 each and uses 3/5 of the sales to buy ingredients to make meat pies for sale on the next day. How much money does Du Chin remain with after setting aside the money for buying ingredients?"""
    # Define the number of meat pies baked and the price per pie
    PIE_PRICE = 20
    NUM_PIES = 200

    # Calculate the total sales
    total_sales = NUM_PIES * PIE_PRICE

    # Calculate the amount used to buy ingredients
    ingredient_cost = total_sales * (3/5)

    # Calculate the remaining amount
    remaining_amount = total_sales - ingredient_cost

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())