def solution():
    regular_calories = 2500
    saturday_extra_calories = 1000
    burn_calories = 3000

    # Calculate the total calories consumed from Sunday to Friday
    total_regular_calories = regular_calories * 6

    # Calculate the total calories consumed on Saturday
    saturday_calories = regular_calories + saturday_extra_calories

    # Calculate the total calories burned in a week
    total_burn_calories = burn_calories * 7

    # Calculate the net caloric deficit in a week
    weekly_deficit = total_burn_calories - (total_regular_calories + saturday_calories)
    result = weekly_deficit
    return result

print(solution())