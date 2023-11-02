def solution():
    total_price = 600000  # The total price of both houses together
    price_ratio = 1/3  # The first house costs one-third of the total price

    # Calculate the price of the first house
    first_house_price = total_price * price_ratio

    result = first_house_price
    return result

print(solution())