def solution():
    """Du Chin bakes 200 meat pies in a day. He sells them for $20 each and uses 3/5 of the sales to buy ingredients to make meat pies for sale on the next day. How much money does Du Chin remain with after setting aside the money for buying ingredients?"""
    # Define the number of meat pies baked and sold
    pies_baked = 200
    pies_sold = 200

    # Define the price per meat pie
    pie_price = 20

    # Calculate the total revenue from selling meat pies
    total_revenue = pies_sold * pie_price

    # Calculate the amount spent on buying ingredients
    ingredient_cost = total_revenue * (3/5)

    # Calculate the profit remaining after buying ingredients
    remaining_profit = total_revenue - ingredient_cost

    result = remaining_profit
    return result

print(solution())