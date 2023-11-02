def solution():
    peak_hours_start = 11
    peak_hours_end = 13
    off_peak_hours_start = 17
    off_peak_hours_end = 18
    cars_per_peak_hour = 12
    cars_per_off_peak_hour = 8
    total_cars = (cars_per_peak_hour * 2) + (cars_per_off_peak_hour * 2)
    result = total_cars
    return result

print(solution())