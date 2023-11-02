def solution():
    """Sam spends sixty minutes studying Science, eighty minutes in Math, and forty minutes in Literature.  How many hours does Sam spend studying the three subjects?"""
    # Define the number of minutes Sam spends studying each subject
    SCIENCE_MINUTES = 60
    MATH_MINUTES = 80
    LIT_MINUTES = 40

    # Calculate the total number of minutes Sam spends studying
    total_minutes = SCIENCE_MINUTES + MATH_MINUTES + LIT_MINUTES

    # Convert the total number of minutes to hours
    total_hours = total_minutes / 60

    # Display the total number of hours Sam spends studying
    result = total_hours
    return result

print(solution())