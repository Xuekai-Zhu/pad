def solution():
    """Frank goes to the store to buy some food. He buys 5 chocolate bars and 2 bags of chips. He hands the cashier $20 and gets $4 back as change. If the chocolate bars each cost $2, how much did each bag of chips cost?"""
    # Define the number of chocolate bars and the cost per bar
    NUM_CHOCOLATE_BARS = 5
    CHOCOLATE_BAR_PRICE = 2

    # Define the amount of money Frank gave the cashier and the change he received
    AMOUNT_PAID = 20
    CHANGE_RECEIVED = 4

    # Calculate the total cost of the chocolate bars
    chocolate_bar_cost = NUM_CHOCOLATE_BARS * CHOCOLATE_BAR_PRICE

    # Calculate the amount spent on chips
    chips_cost = AMOUNT_PAID - chocolate_bar_cost - CHANGE_RECEIVED

    # Calculate the cost per bag of chips
    cost_per_chip_bag = chips_cost / 2

    # Display the cost per bag of chips
    result = cost_per_chip_bag
    return result

print(solution())