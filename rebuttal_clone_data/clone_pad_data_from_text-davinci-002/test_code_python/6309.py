def solution():
    polaroid_cameras = 3
    amazon_price = 20
    maddox_sale_price = 28
    theo_sale_price = 23
    maddox_profit = maddox_sale_price - amazon_price
    theo_profit = theo_sale_price - amazon_price
    result = maddox_profit - theo_profit
    return result

print(solution())