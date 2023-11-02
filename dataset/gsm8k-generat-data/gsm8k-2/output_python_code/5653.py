def solution():
    """Daniel practices basketball for 15 minutes each day during the school week. He practices twice as long each day on the weekend. How many minutes does he practice during a whole week?"""
    school_week_duration = 5
    school_week_minutes = school_week_duration * 15
    weekend_duration = 2
    weekend_minutes = weekend_duration * 15 * 2
    total_minutes = school_week_minutes + weekend_minutes
    result = total_minutes
    return result

print(solution())