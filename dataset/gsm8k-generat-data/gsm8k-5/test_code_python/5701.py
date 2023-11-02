def solution():
    alvin_age = 30  # Alvin is 30 years old
    simon_half_alvin_age = (alvin_age / 2) - 5  # Simon is 5 years away from being 1/2 Alvin's age
    simon_age = simon_half_alvin_age * 2  # Simon's age is twice the difference between his and Alvin's age
    result = simon_age
    return result

print(solution())