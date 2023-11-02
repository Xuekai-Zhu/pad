def solution():
    """Steve spends 1/3 of the day sleeping, 1/6 of the day in school, 1/12 of the day making assignments, and the rest of the day with his family. How many hours does Steve spend with his family in a day?"""
    # Define the fraction of the day spent on each activity
    sleeping_fraction = 1/3
    school_fraction = 1/6
    assignments_fraction = 1/12

    # Calculate the fraction of the day spent with family
    family_fraction = 1 - sleeping_fraction - school_fraction - assignments_fraction

    # Convert the fraction to hours
    hours_with_family = family_fraction * 24

    # Return the result
    result = hours_with_family
    return result

print(solution())