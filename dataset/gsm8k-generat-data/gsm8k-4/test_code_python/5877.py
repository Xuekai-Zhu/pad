def solution():
    """Alexa and Emily open up a lemonade stand in the front yard. They spent $10 for lemons, $5 for sugar and $3 for cups. The lemonade is $4 a cup. They sell a total of 21 cups. How much profit did Alexa and Emily make after paying off expenses?"""
    # Define the cost of lemons, sugar and cups
    lemon_cost = 10
    sugar_cost = 5
    cups_cost = 3

    # Calculate the total cost of ingredients and cups
    total_cost = lemon_cost + sugar_cost + cups_cost

    # Define the price per cup of lemonade
    cup_price = 4

    # Define the number of cups sold
    cups_sold = 21

    # Calculate the total revenue from selling lemonade
    total_revenue = cups_sold * cup_price

    # Calculate the profit after paying off expenses
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())