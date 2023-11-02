def solution():
    black_ink = 2
    black_ink_price = 11
    red_ink = 3
    red_ink_price = 15
    yellow_ink = 2
    yellow_ink_price = 13
    total_price = (black_ink * black_ink_price) + (red_ink * red_ink_price) + (yellow_ink * yellow_ink_price)
    result = total_price - 50
    return result

print(solution())