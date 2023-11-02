def solution():
    chips_price = 40  # The vending machines sell chips for 40 cents
    candy_price = 75  # The vending machines sell candy bars for 75 cents
    total_spent = 5  # George spent $5
    chips_bags = 3  # George got 3 bags of chips
    remaining_money = total_spent - (chips_bags * chips_price)  # George has this much money left
    candy_bars_price = candy_price / candy_bars_price  # Calculate the number of candy bars George bought

    result = candy_bars_price
    return result

print(solution())