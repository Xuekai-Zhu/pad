def solution():
    """Tabitha has 25 dollars. She gives her mom 8 dollars and invests half what is left in a money market. She spends some money on 5 items that costs 50 cents each. How much money does Tabitha have left?"""
    # Define initial amount of money Tabitha has
    initial_amount = 25

    # Subtract money given to mom
    remaining_amount = initial_amount - 8

    # Calculate amount invested in money market
    money_market_amount = remaining_amount / 2

    # Calculate amount spent on items
    items_cost = 5 * 0.5

    # Calculate final remaining amount
    remaining_amount = remaining_amount - money_market_amount - items_cost

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())