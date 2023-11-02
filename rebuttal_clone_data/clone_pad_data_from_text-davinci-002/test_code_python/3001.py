def solution():
    ladies_in_group = 4
    miles_walked = 3
    jamie_additional_miles = 2
    sue_additional_miles = 1
    days_per_week = 6
    total_miles_jamie = jamie_additional_miles * days_per_week
    total_miles_sue = sue_additional_miles * days_per_week
    total_miles_group = (ladies_in_group * miles_walked) + total_miles_jamie + total_miles_sue
    result = total_miles_group
    return result

print(solution())