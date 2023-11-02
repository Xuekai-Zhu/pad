def solution():
    # Calculate the cost of buying the cameras
    cost = 3 * 20

    # Calculate the revenue from Maddox's sales
    maddox_revenue = 3 * 28

    # Calculate the revenue from Theo's sales
    theo_revenue = 3 * 23

    # Calculate the profit for Maddox and Theo
    maddox_profit = maddox_revenue - cost
    theo_profit = theo_revenue - cost

    # Calculate the difference in profit between Maddox and Theo
    difference = maddox_profit - theo_profit
    result = difference
    return result

print(solution())