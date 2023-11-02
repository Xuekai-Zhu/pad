def solution():
    """To produce one chocolate bar, a company needs 1.5 grams of sugar. Every minute the company produces 36 chocolate bars. How many grams of sugar will the company use in two minutes?"""
    # Define the amount of sugar needed to produce one chocolate bar
    SUGAR_PER_BAR = 1.5

    # Define the number of chocolate bars produced per minute
    BARS_PER_MINUTE = 36

    # Calculate the total number of chocolate bars produced in two minutes
    total_bars = 2 * BARS_PER_MINUTE

    # Calculate the total amount of sugar used to produce the chocolate bars
    total_sugar = total_bars * SUGAR_PER_BAR

    # Display the total amount of sugar used
    result = total_sugar 
    return result

print(solution())