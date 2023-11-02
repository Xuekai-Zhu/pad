def solution():
    """Tabitha has 25 dollars. She gives her mom 8 dollars and invests half what is left in a money market. She spends some money on 5 items that costs 50 cents each. How much money does Tabitha have left?"""
    initial_money = 25
    money_given_to_mom = 8
    money_left = initial_money - money_given_to_mom
    money_invested = money_left / 2
    items_bought = 5
    cost_per_item = 0.5
    money_spent = items_bought * cost_per_item
    money_left = money_left - money_spent - money_invested
    result = money_left
    return result

print(solution())