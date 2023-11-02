def solution():
    """John attends a protest for 4 days.  He then attends a second protest for 25% longer than the first.  How many days did he spend protesting?"""
    # Define the duration of the first protest
    first_protest_days = 4

    # Calculate the duration of the second protest
    second_protest_days = first_protest_days * 1.25

    # Calculate the total duration of the protests
    total_days = first_protest_days + second_protest_days

    # Display the total duration of the protests
    result = total_days
    return result

print(solution())