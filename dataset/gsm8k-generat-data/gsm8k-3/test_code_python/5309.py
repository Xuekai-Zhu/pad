def solution():
    """Vivian is responsible for making sure her students get 2 15-minute recess breaks a day, a 30-minute lunch and another 20-minute recess break.  How much time do her students spend outside of class?"""
    # Define the duration of each break
    RECESS_DURATION = 15
    LUNCH_DURATION = 30

    # Calculate the total duration of all the breaks
    total_duration = 2 * RECESS_DURATION + LUNCH_DURATION + 20

    # Display the total duration
    result = total_duration
    return result

print(solution())