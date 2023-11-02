def solution():
    # Calculate the original price of the DVDs Maria bought
    discounted_price = 40  # Maria received a discount of $40
    discount_percentage = 25/100  # Maria received a 25% discount
    original_price = discounted_price / discount_percentage

    # Calculate the total amount Maria paid after the discount
    total_price = original_price - discounted_price
    result = total_price
    return result

print(solution())