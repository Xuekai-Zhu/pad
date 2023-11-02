def solution():
    """The ages of three brothers are consecutive integers with the sum of 96.  How old is the youngest brother?"""
    # Define the sum of the ages of the brothers
    SUM_OF_AGES = 96

    # Define the number of brothers
    NUMBER_OF_BROTHERS = 3

    # Calculate the middle brother's age
    middle_brother_age = SUM_OF_AGES // NUMBER_OF_BROTHERS

    # Calculate the youngest brother's age
    youngest_brother_age = middle_brother_age - 1

    # Display the age of the youngest brother
    result = youngest_brother_age
    return result

print(solution())