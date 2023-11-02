def solution():
    """A gold coin is worth 50 dollars and a silver coin is worth 25 dollars. If you have 3 gold coins, 5 silver coins, and 30 dollars cash, how much money do you have in dollars?"""
    # Define the values of gold and silver coins
    gold_value = 50
    silver_value = 25

    # Calculate the total value of gold coins
    gold_total = 3 * gold_value

    # Calculate the total value of silver coins
    silver_total = 5 * silver_value

    # Calculate the total amount of cash
    cash_total = 30

    # Calculate the total amount of money
    money_total = gold_total + silver_total + cash_total

    # return the result
    result = money_total
    return result

print(solution())