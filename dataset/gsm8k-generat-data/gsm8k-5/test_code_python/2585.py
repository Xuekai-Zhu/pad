def solution():
    full_price = 85  # Duty shoes cost $85 at full price
    discount_1 = 0.2  # Officers who have served at least a year get a 20% discount
    discount_2 = 0.25  # Officers who have served at least three years get an additional 25% off the discounted price

    # Calculate the discounted price for officers who have served at least a year
    discounted_price_1 = full_price - (full_price * discount_1)

    # Calculate the final price for officers who have served at least three years
    final_price = discounted_price_1 - (discounted_price_1 * discount_2)
    result = final_price
    return result

print(solution())