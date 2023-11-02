Unfortunately, there is no solution provided for the Samantha's last name question. As for the Kenny's Pokemon cards question, the solution is as follows:

def solution():
    """Kenny is selling his Pokemon cards to buy a ticket to an amusement park, which costs $100. He has a collection of cards and plans to sell them for $1.5 each. He keeps 1/3 of them and gets to go to the amusement park with $50 in spending cash. How many cards did he start with?"""
    ticket_cost = 100
    spending_cash = 50
    card_price = 1.5
    total_money_needed = ticket_cost + spending_cash
    money_made = total_money_needed / (2/3) # He kept 1/3 of the cards, sold 2/3 of them
    total_cards = money_made / card_price
    result = total_cards
    return result

print(solution())