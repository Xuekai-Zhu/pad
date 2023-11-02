def solution():
    """There are 180 days in a school year. A senior can skip their final exams if they miss 5% or less of the school year. Hazel has missed 6 days of school due to illness. How many more days can she miss and still not have to take her exams?"""
    total_school_days = 180
    allowed_missed_days = total_school_days * 0.05
    remaining_allowed_missed_days = allowed_missed_days - 6
    result = remaining_allowed_missed_days
    return result

print(solution())