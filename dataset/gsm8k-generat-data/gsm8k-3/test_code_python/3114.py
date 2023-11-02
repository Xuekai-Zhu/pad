def solution():
    """Jill sells girl scout cookies. This year, she wants to sell at least 150 cookie boxes. Her first customer buys 5 boxes, her second one buys 4 times more than her first customer. Her third customer buys half as much as her second. The fourth customer buys 3 times as much as her third. Lastly, her final customer buys 10. How many boxes so Jill have left to sell to hit her sales goal?"""
    # Define the number of boxes sold to each customer
    customer1 = 5
    customer2 = customer1 * 4
    customer3 = customer2 / 2
    customer4 = customer3 * 3
    customer5 = 10

    # Calculate the total number of boxes sold
    total_sold = customer1 + customer2 + customer3 + customer4 + customer5

    # Calculate the number of boxes Jill has left to sell to reach her goal of 150
    boxes_left = 150 - total_sold

    # Display the number of boxes Jill has left to sell
    result = boxes_left
    return result

print(solution())