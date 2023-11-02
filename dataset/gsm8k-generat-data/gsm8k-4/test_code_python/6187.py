def solution():
    """The Dow Jones Industrial Average fell 2% today. The Dow ended the day at 8,722. What was the Dow in the morning before the markets opened?"""
    # Define the percentage decrease and the final value of the Dow
    percentage_decrease = 0.02
    dow_final = 8722

    # Calculate the initial value of the Dow
    dow_initial = dow_final / (1 - percentage_decrease)

    # Return the result
    result = dow_initial
    return result

print(solution())