def solution():
    miles_run_by_Jim = 16
    hours_ran_by_Jim = 2
    miles_ran_by_Frank = 20
    hours_ran_by_Frank = 2
    average_miles_per_hour_by_Jim = miles_run_by_Jim / hours_ran_by_Jim
    average_miles_per_hour_by_Frank = miles_ran_by_Frank / hours_ran_by_Frank
    difference_in_miles = average_miles_per_hour_by_Frank - average_miles_per_hour_by_Jim
    result = difference_in_miles
    return result

print(solution())