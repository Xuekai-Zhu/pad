def solution():
    """Mia is a student. In her final year, she spent 1/5 of her day watching TV and 1/4 of the time left on studying. How many minutes did she spend studying each day?"""
    # Define the total number of minutes in a day
    MINUTES_PER_DAY = 1440

    # Calculate the number of minutes Mia spent watching TV
    tv_minutes = MINUTES_PER_DAY / 5

    # Calculate the number of minutes left for studying
    study_minutes_left = MINUTES_PER_DAY - tv_minutes

    # Calculate the number of minutes Mia spent studying
    study_minutes = study_minutes_left / 4

    # Display the number of minutes Mia spent studying
    result = study_minutes
    return result

print(solution())