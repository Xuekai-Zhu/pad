def solution():
    """There are 180 days in a school year. A senior can skip their final exams if they miss 5% or less of the school year. Hazel has missed 6 days of school due to illness. How many more days can she miss and still not have to take her exams?"""
    # Define the total number of days in a school year
    total_days = 180

    # Calculate 5% of the total days
    max_missed_days = total_days * 0.05

    # Calculate the number of missed days
    missed_days = 6

    # Calculate the remaining days Hazel can miss
    remaining_days = max_missed_days - missed_days

    # Display the result
    result = remaining_days
    return result

print(solution())