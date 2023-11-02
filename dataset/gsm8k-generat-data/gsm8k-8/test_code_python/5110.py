def solution():
    total_candy_bars = 12
    snickers = 3
    mars_bars = 2

    # Calculate the number of Butterfingers by subtracting the number of Snickers and Mars bars from the total
    butterfingers = total_candy_bars - snickers - mars_bars

    result = butterfingers
    return result

print(solution())