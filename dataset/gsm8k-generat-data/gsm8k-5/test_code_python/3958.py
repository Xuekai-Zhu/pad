def solution():
    original_price = 125  # The shoes cost $125
    discount_percentage = 0.1  # Mothers receive a 10% discount
    additional_discount_percentage = 0.04  # Mothers with 3 or more children receive an additional 4% off the discounted price
    children = 4  # Mrs. Brown has 4 children

    # Calculate the discounted price for mothers
    discounted_price = original_price * (1 - discount_percentage)

    # Calculate the additional discount for mothers with 3 or more children
    if children >= 3:
        additional_discount = discounted_price * additional_discount_percentage
        discounted_price -= additional_discount

    result = discounted_price
    return result

print(solution())