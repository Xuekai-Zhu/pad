def solution():
    original_price = 25
    discount_percent = 10
    num_guests = 20
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    total_price = final_price * num_guests
    result = total_price
    return result

print(solution())