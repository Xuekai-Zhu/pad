def solution():
    # Calculate Carl's earnings from the neighbor's payment
    weekly_earnings = 0.75
    total_earnings = weekly_earnings * 4

    # Calculate the number of candy bars Carl can buy with his earnings
    candy_bar_cost = 0.5
    candy_bars = total_earnings / candy_bar_cost

    result = candy_bars
    return result

print(solution())