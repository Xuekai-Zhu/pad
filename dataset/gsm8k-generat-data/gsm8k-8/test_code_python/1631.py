def solution():
    #Define John's age and his sister's age
    john_age = 10
    sister_age = 2 * john_age

    #Calculate the age difference between John and his sister
    age_difference = sister_age - john_age

    #Calculate the age difference in 40 years
    age_difference_40_years = age_difference

    #Calculate the sister's age in 40 years from now
    sister_age_40_years = john_age + age_difference_40_years + 40

    result = sister_age_40_years
    return result

print(solution())