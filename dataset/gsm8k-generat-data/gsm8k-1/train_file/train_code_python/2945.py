def solution():
    """Two sisters go to the movies. Movie tickets are $8 per person. If the sisters brought $25 with them, how much change will they receive after buying the tickets?"""
    ticket_price = 8
    total_money = 25
    num_tickets = total_money // ticket_price
    change = total_money - (num_tickets * ticket_price)
    result = change
    return result

print(solution())