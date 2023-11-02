def solution():
    """Mark has 12 candy bars in total between Mars bars, Snickers, and Butterfingers. He has 3 Snickers and 2 Mars bars. How many Butterfingers does he have?"""
    total_bars = 12
    snickers_bars = 3
    mars_bars = 2
    butterfingers_bars = total_bars - (snickers_bars + mars_bars)
    result = butterfingers_bars
    return result

print(solution())