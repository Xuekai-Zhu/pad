def solution():
    ticket_price = 100
    percent_decrease = 20
    decrease_amount = ticket_price * (percent_decrease / 100)
    new_ticket_price = ticket_price - decrease_amount
    result = new_ticket_price
    return result

print(solution())