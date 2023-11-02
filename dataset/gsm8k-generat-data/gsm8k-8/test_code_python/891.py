def solution():
    # Define Katie's daughter's age
    katie_daughter_age = 12

    # Calculate Lavinia's daughter's age
    lavinia_daughter_age = katie_daughter_age - 10

    # Calculate Katie's son's age
    katie_son_age = 2 * katie_daughter_age

    # Calculate Lavinia's son's age
    lavinia_son_age = 2 * lavinia_daughter_age

    # Calculate the age difference between Lavinia's son and daughter
    age_difference = lavinia_son_age - lavinia_daughter_age

    result = age_difference
    return result

print(solution())