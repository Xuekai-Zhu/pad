def solution():
    """The age difference between Asaf and Alexander's age is half the total number of pencils Asaf has. The sum of their ages is 140, and Asaf is 50 years old. If Alexander has 60 more pencils than Asaf, calculate the total number of pencils they have together."""
    # Define Asaf's age and number of pencils
    asaf_age = 50
    asaf_pencils = None # unknown

    # Calculate Alexander's age and number of pencils
    alexander_age = 140 - asaf_age
    alexander_pencils = asaf_pencils + 60

    # Calculate the number of pencils based on the age difference equation
    asaf_alexander_age_diff = abs(asaf_age - alexander_age)
    asaf_pencils = asaf_alexander_age_diff * 2

    # Calculate the total number of pencils
    total_pencils = asaf_pencils + alexander_pencils

    # Display the total number of pencils
    result = total_pencils
    return result

print(solution())