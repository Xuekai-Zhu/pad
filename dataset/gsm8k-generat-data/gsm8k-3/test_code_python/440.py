def solution():
    """Cori is 3 years old today.  In 5 years, she will be one-third the age of her aunt.  How old is her aunt today?"""
    # Define Cori's current age and the number of years in the future
    CORI_AGE = 3
    FUTURE_YEARS = 5

    # Calculate Cori's age in the future
    cori_future_age = CORI_AGE + FUTURE_YEARS

    # Calculate Cori's aunt's age in the future
    aunt_future_age = cori_future_age * 3

    # Calculate Cori's aunt's current age
    aunt_current_age = aunt_future_age - FUTURE_YEARS

    # Display Cori's aunt's current age
    result = aunt_current_age
    return result

print(solution())