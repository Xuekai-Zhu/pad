def solution():
    """Mark has 12 candy bars in total between Mars bars, Snickers, and Butterfingers. He has 3 Snickers and 2 Mars bars. How many Butterfingers does he have?"""
    total_bars = 12
    snickers = 3
    mars = 2
    butterfingers = total_bars - snickers - mars
    result = butterfingers
    return result

print(solution())