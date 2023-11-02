def solution():
    
    time_in_seconds = 6 * 60
    gallons_poured_per_second = 1 / 20
    total_gallons_poured = time_in_seconds * gallons_poured_per_second
    gallons_left_to_fill = 50 - total_gallons_poured
    result = gallons_left_to_fill
    return result

print(solution())