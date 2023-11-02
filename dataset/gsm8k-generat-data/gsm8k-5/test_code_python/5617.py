def solution():
    sister_age = 26  # Kimiko is 26 years old
    kayla_age = sister_age / 2  # Kayla is currently half the age of Kimiko

    # Calculate how many years until Kayla reaches the minimum driving age of 18
    years_until_driving_age = 18 - kayla_age

    result = years_until_driving_age
    return result

print(solution())