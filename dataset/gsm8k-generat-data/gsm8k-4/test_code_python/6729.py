def solution():
    """To produce one chocolate bar, a company needs 1.5 grams of sugar. Every minute the company produces 36 chocolate bars. How many grams of sugar will the company use in two minutes?"""
    # Define the amount of sugar needed to produce one chocolate bar
    sugar_per_bar = 1.5

    # Define the number of chocolate bars produced per minute
    bars_per_minute = 36

    # Calculate the total number of chocolate bars produced in two minutes
    total_bars = bars_per_minute * 2

    # Calculate the total amount of sugar used in two minutes
    total_sugar = sugar_per_bar * total_bars

    # return the result
    result = total_sugar
    return result

print(solution())