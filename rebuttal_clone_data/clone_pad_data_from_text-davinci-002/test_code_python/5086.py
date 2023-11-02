def solution():
    ticket_price = 10
    combo_price = 10
    ticket_discount = 20
    combo_discount = 50
    discount_ticket_price = ticket_price - (ticket_price * (ticket_discount / 100))
    discount_combo_price = combo_price - (combo_price * (combo_discount / 100))
    total_savings = discount_ticket_price + discount_combo_price
    result = total_savings
    return result

print(solution())