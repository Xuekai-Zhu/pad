def solution():
    # Let x be the price of one pair of shoes
    # Then the price of one jersey is 1/4 of x
    # Jeff bought 6 pairs of shoes and 4 jerseys for $560

    total_price = 560
    num_shoes = 6
    num_jerseys = 4
    price_jersey = x / 4

    # Total price equation: 6x + 4(price_jersey) = 560
    # Substitute price_jersey with x/4 and solve for x

    6x + 4(x/4) = 560
    6x + x = 560
    7x = 560
    x = 80

    # The price of one pair of shoes is $80
    # The total price of shoes is 6 pairs * $80/pair = $480

    result = 480
    return result

print(solution())