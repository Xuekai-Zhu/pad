def solution():
    peak_start1 = 11 * 60  # 11:00 in minutes
    peak_end1 = 13 * 60  # 1:00 in minutes
    peak_start2 = 17 * 60  # 5:00 in minutes
    peak_end2 = 18 * 60  # 6:00 in minutes
    off_peak_rate = 8  # cars per 15 minutes
    peak_rate = 12  # cars per 15 minutes
    peak_duration = (peak_end1 - peak_start1) + (peak_end2 - peak_start2)  # in minutes
    off_peak_duration = (1440 - peak_duration - 120) / 15  # remaining time in minutes, minus 2 hours of peak time and divided by 15

    # Calculate number of cars served during peak hours
    peak_cars = (peak_duration / 15) * peak_rate

    # Calculate number of cars served during off-peak hours
    off_peak_cars = off_peak_duration * off_peak_rate

    # Calculate total number of cars served from 4 pm to 6 pm
    total_cars_served = peak_cars + off_peak_cars
    result = total_cars_served
    return result

print(solution())