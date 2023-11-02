def solution():
    sugar_per_chocolate = 1.5
    bars_per_minute = 36
    minutes = 2

    # Calculate the total number of chocolate bars produced in two minutes
    total_bars = bars_per_minute * minutes

    # Calculate the total amount of sugar used in two minutes
    total_sugar = sugar_per_chocolate * total_bars
    result = total_sugar
    return result

print(solution())