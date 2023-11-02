def solution():
    num_cameras = 3
    amazon_price = 20
    maddox_sell_price = 28
    theo_sell_price = 23

    # Calculate the total cost of all cameras bought from Amazon
    total_cost = num_cameras * amazon_price

    # Calculate the total profit of Maddox
    maddox_profit = (num_cameras * maddox_sell_price) - total_cost

    # Calculate the total profit of Theo
    theo_profit = (num_cameras * theo_sell_price) - total_cost

    # Calculate the difference in profit between Maddox and Theo
    profit_diff = maddox_profit - theo_profit
    result = profit_diff
    return result

print(solution())