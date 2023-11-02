def solution():
    """Lavinia’s daughter is 10 years younger than Katie’s daughter. Lavinia’s son is 2 times the age of Katie’s daughter. If Katie’s daughter is 12 years old, how many years older is Lavinia’s son than Lavinia’s daughter?"""
    katie_daughter_age = 12
    lavinia_daughter_age = katie_daughter_age - 10
    lavinia_son_age = katie_daughter_age * 2
    age_difference = lavinia_son_age - lavinia_daughter_age
    result = age_difference
    return result

print(solution())