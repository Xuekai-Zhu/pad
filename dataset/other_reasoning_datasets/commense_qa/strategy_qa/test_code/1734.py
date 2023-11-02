def solution():
    career_start_year = 1995
    career_start_age = 12
    legal_driving_age_in_US_states = {"South Dakota": 14, "New Jersey": 17}
    for state, age in legal_driving_age_in_US_states.items():
        if age <= (career_start_year - career_start_age):
            result = "yes"
            return result
    result = "no"
    return result

print(solution())