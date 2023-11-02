def solution():
    
    initial_mms = 25
    lunch_mms = 7
    dinner_mms = 5
    cheryl_mms = lunch_mms + dinner_mms
    sister_mms = initial_mms - cheryl_mms
    result = sister_mms
    return result

print(solution())