def solution():
    shirt_price = 10

    # If you buy 1 shirt
    total1 = shirt_price

    # If you buy 2 shirts
    total2 = shirt_price + (shirt_price * 0.5)  # Second shirt at 50% off
    total2 -= ((total2 - shirt_price) * 0.5)  # Subtract discount from first shirt

    # If you buy 3 shirts
    total3 = shirt_price + (shirt_price * 0.5) + (shirt_price * 0.4)  # Second shirt at 50% off, third shirt at 60% off
    total3 -= ((total3 - shirt_price - (shirt_price * 0.5)) * 0.5)  # Subtract discount from first two shirts
    total3 -= ((total3 - shirt_price) * 0.6)  # Subtract discount from third shirt

    # Calculate the amount saved by buying 3 shirts
    amount_saved = total1 + total2 + total3 - (shirt_price * 3)
    result = amount_saved
    return result

print(solution())