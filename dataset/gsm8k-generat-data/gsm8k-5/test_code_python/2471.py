def solution():
    nights = 3  # John books 3 nights at the hotel
    price_per_night = 250  # The price per night is $250
    discount = 100  # John has a $100 discount

    # Calculate the total price before discount
    total_price_before_discount = nights * price_per_night

    # Calculate the total price after discount
    total_price_after_discount = total_price_before_discount - discount

    result = total_price_after_discount
    return result

print(solution())