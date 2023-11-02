def solution():
    acres_to_plant = 1700
    days_to_plant = 5
    crew_of_2_tractors = 2
    crew_of_7_tractors = 7
    total_tractors = crew_of_2_tractors + crew_of_7_tractors
    acres_per_day = acres_to_plant / days_to_plant
    acres_per_tractor = acres_per_day / total_tractors
    result = round(acres_per_tractor,2)
    
    return result

print(solution())