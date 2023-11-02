def solution():
    number_of_weeks = 5
    miles_run_per_day = []
    
    for week in range(1, number_of_weeks+1):
        if week == 1:
            miles_run_per_day.append(3)
        else:
            previous_week_miles = miles_run_per_day[week-2]
            miles_run_per_day.append(previous_week_miles+1)
    
    result = miles_run_per_day[-1]
    return result

print(solution())