def solution():
    """The age difference between Asaf and Alexander's age is half the total number of pencils Asaf has. The sum of their ages is 140, and Asaf is 50 years old. If Alexander has 60 more pencils than Asaf, calculate the total number of pencils they have together."""
    # Define Asaf's age and the sum of their ages
    asaf_age = 50
    total_age = 140

    # Calculate Alexander's age
    alexander_age = total_age - asaf_age

    # Calculate the total number of pencils Asaf has
    pencils = asaf_age * 2

    # Calculate the number of pencils Alexander has
    alexander_pencils = pencils + 60

    # Calculate the total number of pencils they have together
    total_pencils = pencils + alexander_pencils

    result = total_pencils
    return result

print(solution())