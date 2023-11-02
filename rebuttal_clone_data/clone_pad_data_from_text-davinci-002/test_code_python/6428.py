def solution():
    hours_swam_before_school = 1
    hours_swam_after_school = 1
    days_swam_before_school = 5
    days_swam_after_school = 5
    hours_swam_on_weekend = 3
    weeks = 4
    total_hours_swam = (hours_swam_before_school * days_swam_before_school) + (hours_swam_after_school * days_swam_after_school) + (hours_swam_on_weekend * weeks)
    result = total_hours_swam
    return result

print(solution())