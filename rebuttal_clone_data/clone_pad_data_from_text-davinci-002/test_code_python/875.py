def solution():
    color_cartridges = 3
    black_and_white_cartridges = 1
    price_color_cartridges = 32
    price_black_and_white_cartridges = 27
    total_price = (color_cartridges * price_color_cartridges) + (black_and_white_cartridges * price_black_and_white_cartridges) 
    result = total_price
    return result

print(solution())