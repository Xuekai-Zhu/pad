def solution():
    earnings_per_candy_bar = 0.5
    earnings_per_week = 0.75

    # Calculate the total earnings after four weeks
    total_earnings = (earnings_per_candy_bar * candy_bars_bought) + (earnings_per_week * 4)

    # Calculate the number of candy bars Carl can buy with his earnings
    num_candy_bars = total_earnings // earnings_per_candy_bar
    result = num_candy_bars
    return result

print(solution())