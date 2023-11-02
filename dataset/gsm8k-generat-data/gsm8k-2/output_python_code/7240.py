def solution():
    """Claire has 400 flowers in her garden. One hundred twenty are tulips, and the rest are roses. Eighty of the roses are white, while the rest are red. Each red rose is worth $0.75. How much will Claire earn if she can sell 1/2 of the total number of red roses?"""
    total_roses = 400 - 120
    white_roses = 80
    red_roses = total_roses - white_roses
    red_roses_value = 0.75
    total_red_roses_value = red_roses_value * red_roses
    half_red_roses = red_roses / 2
    half_red_roses_value = red_roses_value * half_red_roses
    result = half_red_roses_value
    return result

print(solution())