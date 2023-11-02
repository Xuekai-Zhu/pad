def solution():
    total_days = 180   # There are 180 days in a school year
    allowed_missed_days = total_days * 0.05   # A senior can miss 5% or less of the school year to skip final exams
    missed_days = 6   # Hazel has missed 6 days of school
    remaining_allowed_missed_days = allowed_missed_days - missed_days   # Calculate the remaining days Hazel can miss

    result = remaining_allowed_missed_days
    return result

print(solution())