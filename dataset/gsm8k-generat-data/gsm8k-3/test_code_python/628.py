def solution():
    """Alani earned $45 for 3 hours of baby-sitting. At the same rate, for how many hours would she need to baby-sit to earn $75?"""
    # Calculate Alani's hourly rate for baby-sitting
    hourly_rate = 45 / 3

    # Calculate the number of hours she would need to baby-sit to earn $75
    hours_needed = (75 - 45) / hourly_rate

    result = hours_needed
    return result

print(solution())