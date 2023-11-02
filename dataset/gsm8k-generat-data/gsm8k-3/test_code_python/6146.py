def solution():
    """Erika and her brother Rick want to buy a gift for their mother that costs $250. They have both saved money. Erika saved $155 and her brother saved only half of the cost of the gift. They also want to surprise their mother with a birthday cake that costs $25. How much money will they have left after buying their mother a gift and cake?"""
    # Define the cost of the gift and cake
    GIFT_COST = 250
    CAKE_COST = 25

    # Define the amount Erika and Rick saved
    ERIKA_SAVED = 155
    RICK_SAVED = GIFT_COST / 2

    # Calculate the total amount they have to spend
    total_savings = ERIKA_SAVED + RICK_SAVED

    # Calculate the cost of the gift and cake
    total_cost = GIFT_COST + CAKE_COST

    # Calculate the amount of money they have left after buying the gift and cake
    money_left = total_savings - total_cost

    # Display the amount of money they have left
    result = money_left
    return result

print(solution())