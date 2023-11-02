def solution():
    """Mia is a student. In her final year, she spent 1/5 of her day watching TV and 1/4 of the time left on studying. How many minutes did she spend studying each day?"""
    # Define the total number of minutes in a day
    TOTAL_MINUTES = 1440

    # Calculate the number of minutes Mia spends watching TV
    tv_minutes = TOTAL_MINUTES * (1 / 5)

    # Calculate the number of minutes left for studying
    study_minutes = TOTAL_MINUTES - tv_minutes

    # Calculate the number of minutes Mia spends studying
    study_minutes = study_minutes * (1 / 4)

    # Return the result
    result = study_minutes
    return result

print(solution())