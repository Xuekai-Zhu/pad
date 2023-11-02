def solution():
    # Define Tabitha's starting money
    starting_money = 25

    # Subtract the amount Tabitha gave her mom
    after_mom = starting_money - 8

    # Calculate how much Tabitha has left after investing half in the money market
    after_investment = after_mom - (after_mom / 2)

    # Calculate how much Tabitha spent on the 5 items
    item_cost = 0.5
    num_items = 5
    total_item_cost = item_cost * num_items

    # Calculate Tabitha's remaining money
    remaining_money = after_investment - total_item_cost
    result = remaining_money
    return result

print(solution())