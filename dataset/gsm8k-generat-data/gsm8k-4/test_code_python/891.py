def solution():
    """Lavinia’s daughter is 10 years younger than Katie’s daughter. Lavinia’s son is 2 times the age of Katie’s daughter. If Katie’s daughter is 12 years old, how many years older is Lavinia’s son than Lavinia’s daughter?"""
    # Define the age of Katie's daughter
    katie_daughter_age = 12

    # Calculate the age of Lavinia's daughter
    lavinia_daughter_age = katie_daughter_age - 10

    # Calculate the age of Lavinia's son
    lavinia_son_age = katie_daughter_age * 2

    # Calculate the age difference between Lavinia's son and daughter
    age_difference = lavinia_son_age - lavinia_daughter_age

    # Return the result
    result = age_difference
    return result

print(solution())