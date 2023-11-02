def solution():
    
    total_acres = 1700
    total_days = 5
    tractors_day_one = 2
    tractors_day_two = 7
    days_on_first_crew = 2
    days_on_second_crew = 3
    total_tractor_days = (tractors_day_one * days_on_first_crew) + (tractors_day_two * days_on_second_crew)
    acres_per_day_per_tractor = total_acres / total_tractor_days
    result = acres_per_day_per_tractor
    return result

print(solution())