def solution():
    """There are 180 days in a school year.  A senior can skip their final exams if they miss 5% or less of the school year.  Hazel has missed 6 days of school due to illness.  How many more days can she miss and still not have to take her exams?"""
    # Define the total number of school days
    TOTAL_DAYS = 180

    # Calculate the maximum number of days Hazel can miss and not have to take her exams
    max_missed_days = TOTAL_DAYS * 0.05
    remaining_missed_days = max_missed_days - 6

    # Display the remaining number of days Hazel can miss
    result = remaining_missed_days
    return result

print(solution())