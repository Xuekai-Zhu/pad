def solution():
    # Calculate the price increase for the weekend haircut
    weekend_price_increase = 0.5

    # Calculate the price of a weekend haircut
    weekend_haircut_price = (1 + weekend_price_increase) * 18

    # Calculate the price of a Monday haircut
    monday_haircut_price = 18

    # Calculate the difference in price
    price_difference = weekend_haircut_price - monday_haircut_price

    # Calculate the price of the last haircut on Sunday
    sunday_haircut_price = weekend_haircut_price - price_difference

    result = sunday_haircut_price
    return result

print(solution())