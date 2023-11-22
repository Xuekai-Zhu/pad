def solution():
    
    ticket_cost = 100
    sell_price = 1.5
    remaining_cards = ticket_cost / sell_price * (2/3)
    initial_cards = remaining_cards + 50
    result = initial_cards
    return result

print(solution())