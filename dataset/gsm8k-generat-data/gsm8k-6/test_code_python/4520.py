def solution():
    # Calculate the number of colored pencils Cheryl has
    cheryl_pencils = 2 * madeline_pencils  # Cheryl has thrice as many as Cyrus, and Madeline has half of what Cheryl has
    # Calculate the total number of colored pencils
    total_pencils = cheryl_pencils + cyrus_pencils + madeline_pencils
    result = total_pencils
    return result

print(solution())