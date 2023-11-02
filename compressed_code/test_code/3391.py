def solution():
    
    saturday = 80
    monday = saturday - 20
    wednesday = monday + 50
    friday = saturday + monday
    total_audience = saturday + monday + wednesday + friday
    expected_audience = 350
    difference = total_audience - expected_audience
    result = difference
    return result

print(solution())