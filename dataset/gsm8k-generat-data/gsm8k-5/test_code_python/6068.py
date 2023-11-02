def solution():
    starting_amount = 25  # Tabitha starts with $25
    amount_after_giving_mom = starting_amount - 8  # Tabitha gives her mom $8
    amount_after_investment = amount_after_giving_mom / 2  # Tabitha invests half of what is left
    cost_of_items = 5 * 0.5  # Tabitha buys 5 items that cost 50 cents each

    # Calculate the amount of money Tabitha has left
    remaining_amount = amount_after_investment - cost_of_items
    result = remaining_amount
    return result

print(solution())