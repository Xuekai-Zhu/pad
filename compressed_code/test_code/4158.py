def solution():
    
    morning_burn = 4
    start_of_day = 10
    end_of_day = 3
    afternoon_burn = start_of_day - morning_burn - end_of_day
    result = afternoon_burn
    return result

print(solution())