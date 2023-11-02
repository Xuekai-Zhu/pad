def solution():
    # Determine James' age now by adding 3 to his age 3 years ago
    james_age_now = 27 + 3

    # Determine Matt's age in 5 years when he will be twice James' age
    matt_age_in_5_years = james_age_now * 2

    # Determine Matt's current age by subtracting 5 from his age in 5 years
    matt_age_now = matt_age_in_5_years - 5
    result = matt_age_now
    return result

print(solution())