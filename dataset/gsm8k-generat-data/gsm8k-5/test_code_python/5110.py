def solution():
    total_candy_bars = 12  # Mark has 12 candy bars in total
    snickers = 3  # Mark has 3 Snickers bars
    mars_bars = 2  # Mark has 2 Mars bars

    # Calculate the number of Butterfingers Mark has
    butterfingers = total_candy_bars - snickers - mars_bars
    result = butterfingers
    return result

print(solution())