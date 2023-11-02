def solution():
    original_price = 2000  # The original price of the phone
    markup_percentage = 2  # John bought the phone 2% more expensive than Alan

    # Calculate the markup price for John
    markup_price = original_price * (markup_percentage / 100)

    # Calculate the total price John paid
    total_price = original_price + markup_price
    result = total_price
    return result

print(solution())