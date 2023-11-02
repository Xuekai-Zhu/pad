def solution():
    """Claire has 400 flowers in her garden. One hundred twenty are tulips, and the rest are roses. Eighty of the roses are white, while the rest are red. Each red rose is worth $0.75. How much will Claire earn if she can sell 1/2 of the total number of red roses?"""
    total_flowers = 400
    tulips = 120
    roses = total_flowers - tulips
    white_roses = 80
    red_roses = roses - white_roses
    price_per_red_rose = 0.75
    total_red_roses_to_sell = red_roses / 2
    money_earned = total_red_roses_to_sell * price_per_red_rose
    result = money_earned
    return result

print(solution())