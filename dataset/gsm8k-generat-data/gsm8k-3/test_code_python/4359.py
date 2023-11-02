def solution():
    """Steve spends 1/3 of the day sleeping, 1/6 of the day in school, 1/12 of the day making assignments, and the rest of the day with his family. How many hours does Steve spend with his family in a day?"""
    # Define the fractions of the day spent sleeping, in school, and making assignments
    SLEEP_FRACTION = 1/3
    SCHOOL_FRACTION = 1/6
    ASSIGNMENTS_FRACTION = 1/12

    # Define the total amount of time in a day in hours
    TOTAL_HOURS = 24

    # Calculate the total amount of time spent sleeping
    sleep_hours = SLEEP_FRACTION * TOTAL_HOURS

    # Calculate the total amount of time spent in school
    school_hours = SCHOOL_FRACTION * TOTAL_HOURS

    # Calculate the total amount of time spent making assignments
    assignments_hours = ASSIGNMENTS_FRACTION * TOTAL_HOURS

    # Calculate the total amount of time spent with family
    family_hours = TOTAL_HOURS - sleep_hours - school_hours - assignments_hours

    # Display the total amount of time spent with family
    result = family_hours
    return result

print(solution())