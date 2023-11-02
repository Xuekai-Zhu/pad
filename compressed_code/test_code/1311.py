def solution():
    
    monday_rain = 1.5
    tuesday_rain = 2.5
    monday_total = monday_rain * 7
    tuesday_total = tuesday_rain * 9
    difference = tuesday_total - monday_total
    result = difference
    return result

print(solution())