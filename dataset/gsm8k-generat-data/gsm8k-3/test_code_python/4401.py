def solution():
    """Alice needs to sell $1000 of shoes to meet her quota. Adidas cost $45, Nike cost $60, and Reeboks cost $35. If she sells 8 Nikes, 6 Adidas's, and 9 Reeboks, how much is she short or above her goal?"""
    # Define the cost of each type of shoe
    ADIDAS_PRICE = 45
    NIKE_PRICE = 60
    REEBOK_PRICE = 35

    # Define the number of each type of shoe sold
    adidas_sold = 6
    nike_sold = 8
    reebok_sold = 9

    # Calculate the total revenue from each type of shoe
    adidas_revenue = adidas_sold * ADIDAS_PRICE
    nike_revenue = nike_sold * NIKE_PRICE
    reebok_revenue = reebok_sold * REEBOK_PRICE

    # Calculate the total revenue from all shoes sold
    total_revenue = adidas_revenue + nike_revenue + reebok_revenue

    # Calculate the difference between the total revenue and the goal
    difference = total_revenue - 1000

    # Display whether Alice is short or above her goal and by how much
    if difference < 0:
        result = "Alice is short by $" + str(abs(difference))
    elif difference > 0:
        result = "Alice is above her goal by $" + str(difference)
    else:
        result = "Alice met her goal exactly!"

    return result

print(solution())