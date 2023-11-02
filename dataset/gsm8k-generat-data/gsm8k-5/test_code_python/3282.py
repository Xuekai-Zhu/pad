def solution():
    # Calculate Mark's age in February 2021
    mark_age = 2021 - 1976  # Mark was born in January 1976

    # Calculate Graham's age in February 2021
    graham_age = mark_age - 3  # Graham is 3 years younger than Mark

    # Calculate Janice's age in February 2021
    janice_age = 0.5 * graham_age  # Janice is 1/2 the age of Graham

    result = janice_age
    return result

print(solution())