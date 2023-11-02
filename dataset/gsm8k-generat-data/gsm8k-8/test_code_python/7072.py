def solution():
    # Determine Divya's age in 5 years
    divya_future_age = 5 + 5  # Divya is currently 5 years old

    # Calculate Nacho's age in 5 years
    nacho_future_age = 3 * divya_future_age

    # Calculate Nacho's current age
    nacho_age = nacho_future_age - 5

    # Calculate the sum of their current ages
    total_age = nacho_age + 5

    result = total_age
    return result

print(solution())