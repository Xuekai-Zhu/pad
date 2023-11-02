def solution():
    """Mike is 16 years old. His sister Barbara is half as old as he is. How old is Barbara going to be when Mike is 24 years old?"""
    # Define the current ages of Mike and Barbara
    mike_age = 16
    barbara_age = mike_age / 2

    # Define the age difference between Mike and Barbara
    age_difference = mike_age - barbara_age

    # Calculate the number of years until Mike is 24
    years_until_24 = 24 - mike_age

    # Calculate how old Barbara will be when Mike is 24
    barbara_age_in_24 = barbara_age + years_until_24

    result = barbara_age_in_24
    return result

print(solution())