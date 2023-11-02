def solution():
    """A gold coin is worth 50 dollars and a silver coin is worth 25 dollars. If you have 3 gold coins, 5 silver coins, and 30 dollars cash, how much money do you have in dollars?"""
    # Define the values of a gold and silver coin
    GOLD_VALUE = 50
    SILVER_VALUE = 25

    # Define the number of gold and silver coins
    num_gold_coins = 3
    num_silver_coins = 5

    # Calculate the total value of the gold coins
    gold_total = num_gold_coins * GOLD_VALUE

    # Calculate the total value of the silver coins
    silver_total = num_silver_coins * SILVER_VALUE

    # Calculate the total amount of money
    total_money = gold_total + silver_total + 30

    # Display the total amount of money
    result = total_money
    return result

print(solution())