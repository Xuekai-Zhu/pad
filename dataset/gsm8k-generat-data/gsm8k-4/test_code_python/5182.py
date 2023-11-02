def solution():
    """While at Wizards Park, Kate buys 3 magic wands, one for herself and two for her friends. When she returns she sells the wands to her friends for $5 more than she paid. If she collected $130 after the sale, how much money did each wand cost?"""
    # Define the number of wands bought and the profit per wand
    wands_bought = 3
    profit_per_wand = 5

    # Calculate the total money collected from the sale
    total_money = 130

    # Calculate the total cost of the wands before the sale
    total_cost = total_money - (wands_bought * profit_per_wand)

    # Calculate the cost of one wand
    wand_cost = total_cost / wands_bought

    # Return the cost of one wand
    result = wand_cost
    return result

print(solution())