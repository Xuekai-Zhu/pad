def solution():
    total_water_for_week = 60
    water_per_day = {
        "Monday": 9,
        "Tuesday": 8,
        "Wednesday": None,
        "Thursday": 9,
        "Friday": 8,
        "Saturday": 9,
        "Sunday": 8
    }

    # Calculate the total water intake for all the days except Wednesday
    total_water_except_wed = sum([water_per_day[d] for d in water_per_day if d != "Wednesday"])

    # Calculate the water intake for Wednesday by subtracting total intake from total for the week
    water_on_wednesday = total_water_for_week - total_water_except_wed
    result = water_on_wednesday
    return result

print(solution())