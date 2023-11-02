def solution():
    """Daria wants to go to a concert by her favorite band. She wants to buy tickets for her and for three of her friends. One ticket cost is $90. How much money does Daria need to earn if she currently has only $189?"""
    num_tickets = 4
    ticket_price = 90
    current_money = 189
    total_cost = num_tickets * ticket_price
    money_needed = total_cost - current_money
    result = money_needed
    return result

print(solution())