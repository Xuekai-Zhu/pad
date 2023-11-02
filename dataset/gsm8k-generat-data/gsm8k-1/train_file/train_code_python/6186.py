def solution():
    """The Dow Jones Industrial Average fell 2% today. The Dow ended the day at 8,722. What was the Dow in the morning before the markets opened?"""
    end_of_day_dow = 8722
    percent_fall = 2
    starting_dow = end_of_day_dow / (1 - (percent_fall / 100))
    result = starting_dow
    return result

print(solution())