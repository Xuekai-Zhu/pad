def solution():
    """Daniel practices basketball for 15 minutes each day during the school week. He practices twice as long each day on the weekend. How many minutes does he practice during a whole week?"""
    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Define the number of minutes Daniel practices during the school week
    school_week_practice = 15 * 5

    # Define the number of minutes Daniel practices on the weekend
    weekend_practice = 15 * 2 * 2

    # Calculate the total number of minutes Daniel practices in a week
    total_practice = school_week_practice + weekend_practice

    # Multiply the total practice time by the number of days in a week
    weekly_practice = total_practice * DAYS_IN_WEEK

    result = weekly_practice
    return result

print(solution())