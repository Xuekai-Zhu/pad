def solution():
    """The Dow Jones Industrial Average fell 2% today. The Dow ended the day at 8,722. What was the Dow in the morning before the markets opened?"""
    current_dow = 8722
    percent_change = 2
    previous_dow = current_dow / (1 - percent_change/100)
    result = previous_dow
    return result

print(solution())