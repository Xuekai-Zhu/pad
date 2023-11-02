def solution():
    # Define the number of guests and the price per person
    guests = 20
    price_per_person = 25.00

    # Calculate the total price without the discount
    total_price = guests * price_per_person

    # Apply the repeat customer discount
    repeat_customer_discount = 0.10
    if guests >= 10:
        total_price -= repeat_customer_discount * total_price

    result = total_price
    return result

print(solution())