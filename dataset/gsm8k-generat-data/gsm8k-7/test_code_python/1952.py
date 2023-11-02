def solution():
    num_candy_bars = 10  # On the first day
    candy_bar_price = 0.1  # 10 cents
    num_days = 6

    # Calculate the total number of candy bars sold in a week
    total_candy_bars = num_candy_bars
    for i in range(1, num_days):
        num_candy_bars += 4  # Sell four more candy bars than the previous day
        total_candy_bars += num_candy_bars

    # Calculate the total earnings from selling candy bars in a week
    total_earnings = total_candy_bars * candy_bar_price
    result = total_earnings
    return result

print(solution())