def solution():
    total_pencils = (50 * 2) * 2  # Age difference is half the total number of pencils Asaf has
    alex_pencils = total_pencils + 60  # Alexander has 60 more pencils than Asaf
    alex_age = (140 - 50) / 2  # Sum of their ages is 140, and we know Asaf's age is 50
    asaf_age = 50
    total_pencils = alex_pencils + total_pencils  # Calculate total number of pencils
    result = total_pencils
    return result

print(solution())