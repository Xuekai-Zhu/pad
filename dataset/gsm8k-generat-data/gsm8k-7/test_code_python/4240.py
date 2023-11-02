def solution():
    diane_current_age = 16

    # Calculate the age that Diane will turn 30
    diane_turning_30_age = 30

    # Calculate Alex's age when Diane turns 30
    alex_age_turning_30 = diane_turning_30_age * 2

    # Calculate Allison's age when Diane turns 30
    allison_age_turning_30 = diane_turning_30_age / 2

    # Calculate how many years in the future we need to go to reach when Diane turns 30
    num_years_until_diane_turns_30 = diane_turning_30_age - diane_current_age

    # Calculate Alex's current age
    alex_current_age = alex_age_turning_30 - num_years_until_diane_turns_30

    # Calculate Allison's current age
    allison_current_age = allison_age_turning_30 - num_years_until_diane_turns_30

    # Calculate the sum of Alex and Allison's current ages
    sum_of_alex_and_allison_ages = alex_current_age + allison_current_age
    result = sum_of_alex_and_allison_ages
    return result

print(solution())