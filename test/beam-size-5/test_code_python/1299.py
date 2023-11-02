def solution():
    holes_per_day = 6  # Nate's dog can dig 6 holes a day
    days_digging = 14  # Nate digs for 14 days
    holes_filled_per_day = 9  # Nate fills in 9 holes a day when Nate gets home
    new_holes_per_night = 6  # Nate keeps 6 new holes every night

    # Calculate the total number of holes Nate needs to dig
    total_holes = holes_per_day * days_digging

    # Calculate the total number of weeks it will take Nate to fill all the holes
    total_weeks = total_holes / holes_per_week
    result = total_weeks
    return result

print(solution())