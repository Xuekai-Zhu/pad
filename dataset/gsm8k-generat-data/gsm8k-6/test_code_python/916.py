def solution():
    # Calculate the number of pencils Asaf has
    age_difference = 140 - 50 - 60  # the age difference between Asaf and Alexander's age is half the total number of pencils Asaf has, and Alexander has 60 more pencils than Asaf
    asaf_pencils = 2 * age_difference

    # Calculate the total number of pencils they have together
    total_pencils = asaf_pencils + 60  # Alexander has 60 more pencils than Asaf
    result = total_pencils
    return result

print(solution())