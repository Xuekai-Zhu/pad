def solution():
    """The Dow Jones Industrial Average fell 2% today. The Dow ended the day at 8,722. What was the Dow in the morning before the markets opened?"""

    # Define the percentage decrease and the ending Dow
    percent_decrease = 0.02
    ending_dow = 8722

    # Calculate the original Dow before the decrease
    original_dow = ending_dow / (1 - percent_decrease)

    # Display the original Dow
    result = original_dow
    return result

print(solution())