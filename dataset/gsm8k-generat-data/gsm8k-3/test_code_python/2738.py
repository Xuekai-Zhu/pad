def solution():
    """Marj has two $20 bills, three $5 bills, and $4.50 in loose coins in her wallet. If she buys a cake that costs $17.50, how much money will be left in her wallet?"""
    # Define the value of each bill and coin
    TWENTY_DOLLAR = 20
    FIVE_DOLLAR = 5
    LOOSE_COINS = 0.25

    # Define the number of each bill and the total amount of loose coins in Marj's wallet
    num_twenty_dollars = 2
    num_five_dollars = 3
    loose_coins_total = 4.50

    # Calculate the total amount of money in Marj's wallet
    total_money = (num_twenty_dollars * TWENTY_DOLLAR) + (num_five_dollars * FIVE_DOLLAR) + loose_coins_total

    # Subtract the cost of the cake from the total amount of money to find out how much Marj will have left
    money_left = total_money - 17.50

    # Display the amount of money left in Marj's wallet
    result = money_left
    return result

print(solution())