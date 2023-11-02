def solution():
    """Tabitha has 25 dollars. She gives her mom 8 dollars and invests half what is left in a money market. She spends some money on 5 items that costs 50 cents each. How much money does Tabitha have left?"""
    starting_amount = 25
    amount_given_to_mom = 8
    remaining_amount = starting_amount - amount_given_to_mom
    money_market_amount = remaining_amount * 0.5
    items_cost = 5 * 0.5
    final_amount = remaining_amount - money_market_amount - items_cost
    result = final_amount
    return result

print(solution())