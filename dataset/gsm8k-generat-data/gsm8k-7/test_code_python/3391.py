def solution():
    total_days = 21
    travel_days = 5
    grandparents_days = 5
    brother_days = 5
    sister_travel_days = 2
    sister_stay_days = total_days - (travel_days*2 + grandparents_days + brother_days + sister_travel_days*2) # calculate the remaining days
    result = sister_stay_days
    return result

print(solution())