def solution():
    """Olivia and Nigel are traveling in Asia. Olivia has $112 and Nigel has $139. If together they buy six one day passes to a tourist attraction for $28 per ticket, how much money do they have left?"""
    olivia_money = 112
    nigel_money = 139
    total_money = olivia_money + nigel_money
    num_tickets = 6
    ticket_price = 28
    total_spent = num_tickets * ticket_price
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())