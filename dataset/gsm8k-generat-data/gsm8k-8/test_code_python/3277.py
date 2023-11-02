def solution():
    # Calculate Jane's age in six years
    jane_future_age = 28 + 6

    # Calculate Dara's current age
    dara_age = 0.5 * (jane_future_age - 6)

    # Calculate how many years until Dara reaches the minimum employment age
    years_until_minimum_age = 25 - dara_age
    result = years_until_minimum_age
    return result

print(solution())