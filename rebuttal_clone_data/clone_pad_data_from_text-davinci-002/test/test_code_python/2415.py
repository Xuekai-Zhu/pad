def solution():
    regular_price = 15
    discount = 40
    discount_amount = regular_price * (discount / 100)
    ticket_price = regular_price - discount_amount
    result = ticket_price
    return result

print(solution())