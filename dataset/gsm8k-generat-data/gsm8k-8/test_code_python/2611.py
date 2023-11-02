def solution():
    # Define Trevor's current age and his older brother's age
    trevor_age = 11
    older_brother_age = 20

    # Calculate the difference in age between Trevor and his older brother
    age_difference = older_brother_age - trevor_age

    # Calculate the age when the older brother will be three times as old as Trevor is now
    triple_trevor_age = age_difference * 3 + trevor_age

    # Calculate how many years from now that will be
    years_from_now = triple_trevor_age - trevor_age

    result = years_from_now
    return result

print(solution())