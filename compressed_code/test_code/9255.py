def solution():
    
    total_miles = 5
    uphill_percent = 60
    downhill_percent = 100 - uphill_percent
    uphill_miles = total_miles * (uphill_percent / 100)
    downhill_miles = total_miles - uphill_miles
    uphill_time = uphill_miles / 2
    downhill_time = downhill_miles / 3
    total_time = uphill_time + downhill_time
    total_time_in_minutes = total_time * 60
    result = total_time_in_minutes
    return result

print(solution())