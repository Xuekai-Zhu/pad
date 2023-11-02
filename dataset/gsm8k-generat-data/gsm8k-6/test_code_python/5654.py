def solution():
    # Calculate the total minutes Daniel practices during the school week
    school_week_minutes = 15 * 5  # he practices for 15 minutes each day during the school week

    # Calculate the total minutes Daniel practices during the weekend
    weekend_minutes = 2 * 15 * 2  # he practices twice as long each day on the weekend, and there are 2 weekend days

    # Calculate the total minutes Daniel practices during the whole week
    total_minutes = school_week_minutes + weekend_minutes
    result = total_minutes
    return result

print(solution())