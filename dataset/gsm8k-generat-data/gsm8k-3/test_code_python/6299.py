def solution():
    """Ariel began fencing in 2006. If she was born in 1992 and has been fencing for 16 years, how old is she now?"""
    # Calculate the year Ariel was born
    birth_year = 1992

    # Calculate the current year
    current_year = 2022

    # Calculate the number of years since Ariel began fencing
    years_fencing = 16

    # Calculate Ariel's current age
    age = current_year - birth_year + years_fencing

    # Display Ariel's current age
    result = age
    return result

print(solution())