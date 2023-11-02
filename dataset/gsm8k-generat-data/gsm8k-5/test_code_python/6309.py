def solution():
    price_per_camera = 20  # The cameras were sold for $20 each
    number_of_cameras = 3  # Maddox and Theo both bought 3 cameras each

    # Maddox's profit
    maddox_profit = (28 - price_per_camera) * number_of_cameras

    # Theo's profit
    theo_profit = (23 - price_per_camera) * number_of_cameras

    # Difference in profit
    profit_difference = maddox_profit - theo_profit
    result = profit_difference
    return result

print(solution())