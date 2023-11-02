def solution():
    """Jill sells girl scout cookies. This year, she wants to sell at least 150 cookie boxes. 
    Her first customer buys 5 boxes, Her second one buys 4 times more than her first customer. 
    Her third customer buys half as much as her second. The fourth customer buys 3 times as much
    as her third. Lastly, her final customer buys 10. How many boxes so Jill have left to sell
    to hit her sales goal?"""

    # Define the sales goal and initialize the total sold boxes
    sales_goal = 150
    total_sold = 0

    # Sell cookies to the first customer
    total_sold += 5

    # Sell cookies to the second customer
    total_sold += 4 * 5

    # Sell cookies to the third customer
    total_sold += (4 * 5) / 2

    # Sell cookies to the fourth customer
    total_sold += 3 * ((4 * 5) / 2)

    # Sell cookies to the fifth customer
    total_sold += 10

    # Calculate the number of boxes left to sell to reach the sales goal
    boxes_left = sales_goal - total_sold

    # Return the result
    result = boxes_left
    return result

print(solution())