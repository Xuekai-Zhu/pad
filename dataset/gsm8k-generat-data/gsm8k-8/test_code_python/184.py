def solution():
    # Calculate the total number of positive cases after the second day
    num_cases_day2 = 2000 + 500
    num_recoveries_day2 = 50
    total_cases_day2 = num_cases_day2 - num_recoveries_day2
    
    # Calculate the total number of positive cases after the third day
    num_cases_day3 = 1500
    num_recoveries_day3 = 200
    total_cases_day3 = total_cases_day2 + num_cases_day3 - num_recoveries_day3
    
    result = total_cases_day3
    return result

print(solution())