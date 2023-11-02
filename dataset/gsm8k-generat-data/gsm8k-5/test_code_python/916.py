def solution():
    # Given information
    asaf_age = 50
    total_pencils = asaf_age * 2
    alex_pencils = total_pencils + 60
    total_age = 140

    # Calculate Alexander's age using the given information
    alex_age = total_age - asaf_age
    # Calculate Asaf's age difference with Alexander
    age_diff = abs(asaf_age - alex_age)
    # Check if the age difference is indeed half the number of pencils Asaf has
    if age_diff == total_pencils / 2:
        # Calculate the total number of pencils they have together
        total_pencils_together = total_pencils + alex_pencils
        result = total_pencils_together
    else:
        result = "Invalid information given"
    return result

print(solution())