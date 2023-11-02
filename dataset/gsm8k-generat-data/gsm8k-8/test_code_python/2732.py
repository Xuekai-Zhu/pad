def solution():
    # Define the number of loaves baked per hour per oven and the number of ovens
    loaves_per_hour_per_oven = 5
    num_of_ovens = 4

    # Calculate the number of loaves baked per day for weekdays and weekend days
    loaves_per_weekday = (5 * loaves_per_hour_per_oven * num_of_ovens)
    loaves_per_weekendday = (2 * loaves_per_hour_per_oven * num_of_ovens)

    # Calculate the total number of loaves baked in a week
    total_loaves_per_week = (loaves_per_weekday * 5) + (loaves_per_weekendday * 2)

    # Calculate the total number of loaves baked in 3 weeks
    total_loaves = total_loaves_per_week * 3

    result = total_loaves
    return result

print(solution())