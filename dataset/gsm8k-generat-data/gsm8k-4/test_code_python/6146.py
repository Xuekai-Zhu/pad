def solution():
    """Erika and her brother Rick want to buy a gift for their mother that costs $250. They have both saved money. Erika saved $155 and her brother saved only half of the cost of the gift. They also want to surprise their mother with a birthday cake that costs $25. How much money will they have left after buying their mother a gift and cake?"""
    # Define the cost of the gift and the cost of the cake
    gift_cost = 250
    cake_cost = 25

    # Define the amount of money saved by Erika and her brother
    erika_savings = 155
    rick_savings = gift_cost / 2

    # Calculate the total amount of money they have
    total_money = erika_savings + rick_savings

    # Calculate the amount of money left after buying the gift and the cake
    money_left = total_money - gift_cost - cake_cost

    result = money_left
    return result

print(solution())