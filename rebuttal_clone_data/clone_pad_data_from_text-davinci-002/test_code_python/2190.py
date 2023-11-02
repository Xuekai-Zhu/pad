def solution():
    ticket_cost = 50
    entrée_cost = 10
    drink_cost = 30
    refund_percent = 90
    total_cost = (ticket_cost + entrée_cost) + (drink_cost * 0.5)
    refund_amount = total_cost * (refund_percent / 100)
    money_lost = total_cost - refund_amount
    result = money_lost
    return result

print(solution())