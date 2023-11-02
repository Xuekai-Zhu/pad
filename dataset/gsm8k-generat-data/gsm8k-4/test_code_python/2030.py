def solution():
    """On Tuesday, a fruit vendor sold 2.5 dozen lemons and 5 dozens avocados. What is the total number of fruits that the fruit vendor sold?"""
    # Define the number of fruits in a dozen
    FRUITS_PER_DOZEN = 12

    # Calculate the total number of lemons sold
    lemons_sold = 2.5 * FRUITS_PER_DOZEN

    # Calculate the total number of avocados sold
    avocados_sold = 5 * FRUITS_PER_DOZEN

    # Calculate the total number of fruits sold
    total_fruits_sold = lemons_sold + avocados_sold

    result = total_fruits_sold
    return result

print(solution())