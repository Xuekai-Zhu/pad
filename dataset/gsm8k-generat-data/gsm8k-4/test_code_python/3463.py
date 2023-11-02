def solution():
    """John buys thank you cards. He decides to buy them for people who got him Christmas and birthday presents. He sent 20 for Christmas gifts and 15 for birthday gifts. If each card cost $2 how much did he spend on cards?"""
    # Define the number of cards for Christmas and birthday gifts
    christmas_cards = 20
    birthday_cards = 15

    # Define the cost per card
    cost_per_card = 2

    # Calculate the total cost of the cards
    total_cost = christmas_cards * cost_per_card + birthday_cards * cost_per_card

    # return the result
    result = total_cost
    return result

print(solution())