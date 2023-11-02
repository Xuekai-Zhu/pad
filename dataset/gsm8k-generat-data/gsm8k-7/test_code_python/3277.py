def solution():
    minimum_age = 25
    jane_current_age = 28
    dara_future_age = jane_current_age/2 + 6 # Dara will be half Jane's age in 6 years
    years_until_minimum_age = minimum_age - dara_future_age
    result = years_until_minimum_age
    return result

print(solution())