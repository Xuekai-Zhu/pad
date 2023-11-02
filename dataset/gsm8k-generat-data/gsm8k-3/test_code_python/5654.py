def solution():
    """Daniel practices basketball for 15 minutes each day during the school week. He practices twice as long each day on the weekend. How many minutes does he practice during a whole week?"""
    # Define the number of minutes Daniel practices during the school week
    school_week_minutes = 15 * 5

    # Define the number of minutes Daniel practices during the weekend
    weekend_minutes = 15 * 2 * 2

    # Calculate the total number of minutes Daniel practices during the week
    total_minutes = school_week_minutes + weekend_minutes

    # Display the total number of minutes Daniel practices
    result = total_minutes
    return result

print(solution())