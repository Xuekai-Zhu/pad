def solution():
    num_pencils = 20  # The store sold 20 pencils

    # Let x be the price of one pencil
    # Then the price of 2 erasers is 1/2 * x, or 0.5x
    # The total cost of buying 1 pencil and 2 erasers is 1.5x
    # The store earned $80 from selling pencils, so 20 * 1.5x = 80
    # Solving for x, we get x = $2

    price_pencil = 2  # The price of one pencil is $2
    price_erasers = 0.5 * price_pencil  # The price of 2 erasers is half the price of one pencil

    result = price_erasers
    return result

print(solution())