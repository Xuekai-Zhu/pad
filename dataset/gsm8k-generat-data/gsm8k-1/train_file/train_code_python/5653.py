def solution():
    """Daniel practices basketball for 15 minutes each day during the school week. He practices twice as long each day on the weekend. How many minutes does he practice during a whole week?"""
    school_days = 5
    weekend_days = 2
    school_minutes = 15
    weekend_minutes = school_minutes * 2
    total_minutes = (school_days * school_minutes) + (weekend_days * weekend_minutes)
    result = total_minutes
    return result

print(solution())