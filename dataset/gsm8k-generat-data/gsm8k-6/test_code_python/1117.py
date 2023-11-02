def solution():
    # Calculate the age of Billy
    age_Gladys = 30  # given in the problem
    age_Billy = age_Gladys / 3  # given in the problem
    age_Lucas = (age_Gladys - 2* (age_Billy)) / 2  # Gladys's age is twice the sum of Billy and Lucas's age

    # Calculate the age of Lucas after three years
    age_Lucas_in_3_years = age_Lucas + 3
    result = age_Lucas_in_3_years
    return result

print(solution())