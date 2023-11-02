def solution():
    
    total_days = 21
    travel_days = 1 + 1 + 2
    grandparents_days = 5
    brother_days = 5
    sister_travel_days = 2
    sister_house_days = total_days - travel_days - grandparents_days - brother_days - sister_travel_days
    result = sister_house_days
    return result

print(solution())