def solution():
    earth_day_month = "April"
    summer_months = ["June", "July", "August", "September"]
    if earth_day_month in summer_months:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())