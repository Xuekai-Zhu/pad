def solution():
    northern_summer_months = ["June", "July", "August"]
    southern_winter_months = ["June", "July", "August"]
    overlap = [month for month in northern_summer_months if month in southern_winter_months]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())