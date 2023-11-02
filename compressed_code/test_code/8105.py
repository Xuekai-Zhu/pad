def solution():
    
    price_per_person = 25
    repeat_customer_discount = 0.1
    num_guests = 20
    total_price = num_guests * price_per_person
    if num_guests >= 10:
        discount_amount = repeat_customer_discount * total_price
        total_price = total_price - discount_amount
    result = total_price
    return result

print(solution())