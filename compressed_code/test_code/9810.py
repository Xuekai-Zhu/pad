def solution():
    
    gallons_per_minute = 20
    total_gallons = 4000
    firefighters = 5
    time_in_minutes = total_gallons / (firefighters * gallons_per_minute)
    result = time_in_minutes
    return result

print(solution())