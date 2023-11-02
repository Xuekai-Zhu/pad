def solution():
    """Mike is 16 years old. His sister Barbara is half as old as he is. How old is Barbara going to be when Mike is 24 years old?"""
    # Calculate Barbara's age relative to Mike's age
    age_difference = 16 - (16 / 2)

    # Calculate how many years it will take for Mike to be 24 years old
    years_to_24 = 24 - 16

    # Add the number of years to Barbara's age difference to get her age when Mike is 24
    barbara_age = age_difference + years_to_24

    # Display Barbara's age when Mike is 24
    result = barbara_age
    return result

print(solution())