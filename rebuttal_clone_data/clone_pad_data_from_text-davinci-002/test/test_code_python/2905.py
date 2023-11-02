def solution():
    gallons_per_minute = 20
    gallons_needed = 4000
    firefighters = 5
    total_gallons = firefighters * gallons_per_minute
    minutes_needed = gallons_needed / total_gallons
    result = minutes_needed
    return result

print(solution())