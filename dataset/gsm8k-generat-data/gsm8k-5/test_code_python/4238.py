def solution():
    sandwich_price = 8  # The original price of the sandwich is $8
    discount = sandwich_price / 4  # Luca had a coupon for a quarter off the price
    upgraded_sandwich_price = sandwich_price - discount + 1  # Luca upgraded his sandwich with sliced avocado for an extra dollar
    drink_and_salad_price = 3 + upgraded_sandwich_price  # The total price of the drink and salad is $3 + the price of the upgraded sandwich
    total_price = 12  # The total lunch bill is $12

    # Calculate how much Luca paid for his drink
    drink_price = total_price - drink_and_salad_price
    result = drink_price
    return result

print(solution())