def solution():
    luke_age = 20
    bernard_age = 3 * (luke_age + 8)

    # Calculate the average age of Luke and Bernard in 8 years
    avg_age_in_8_years = (luke_age + 8 + bernard_age + 8) / 2

    # Calculate the desired result
    result = avg_age_in_8_years - 10
    return result

print(solution())