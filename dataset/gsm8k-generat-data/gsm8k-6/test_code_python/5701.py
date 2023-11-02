def solution():
    # Calculate Simon's age using the given information
    half_Alvin_age = 2*(Alvin_age + 5)  # Simon is 5 years away from being 1/2 the age of Alvin
    Simon_age = half_Alvin_age - 5
    result = Simon_age
    return result

print(solution())