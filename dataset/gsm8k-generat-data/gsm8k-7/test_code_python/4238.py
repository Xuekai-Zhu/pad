def solution():
    original_sandwich_price = 8
    discount = 0.25  # 25% discount
    upgraded_price = 9
    salad_price = 3
    total_price = 12

    # Calculate the price of the sandwich after discount and upgrade
    sandwich_price = original_sandwich_price * (1 - discount) + upgraded_price

    # Calculate the price of the drink
    drink_price = total_price - (salad_price + sandwich_price)
    result = drink_price
    return result

print(solution())