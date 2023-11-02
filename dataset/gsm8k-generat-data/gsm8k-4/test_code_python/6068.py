def solution():
    """Tabitha has 25 dollars. She gives her mom 8 dollars and invests half what is left in a money market. She spends some money on 5 items that costs 50 cents each. How much money does Tabitha have left?"""
    # Define Tabitha's initial amount of money
    initial_money = 25

    # Calculate the amount of money left after giving 8 dollars to her mom
    money_left = initial_money - 8

    # Calculate the amount of money to invest in a money market
    money_market = money_left / 2

    # Calculate the total cost of the 5 items she bought
    item_cost = 0.5 * 5

    # Calculate the amount of money left after buying the items
    money_left -= item_cost

    # Calculate the final amount of money she has
    final_money = money_left + money_market

    result = final_money
    return result

print(solution())