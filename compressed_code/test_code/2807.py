def solution():
    
    fiona_hours = 40
    john_hours = 30
    jeremy_hours = 25
    hourly_rate = 20
    total_hours = fiona_hours + john_hours + jeremy_hours
    total_pay = total_hours * hourly_rate * 4  
    result = total_pay
    return result

print(solution())