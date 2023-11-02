def solution():
    # Calculate the number of 15-minute intervals during peak and off-peak times
    peak_intervals = (2 * 4) + (1 * 1)  # 2 hours of peak time + 1 hour of overlap
    off_peak_intervals = (2 * 3) + (1 * 1)  # 2 hours of off-peak time + 1 hour of overlap

    # Calculate the total number of cars served during peak and off-peak times
    peak_cars = peak_intervals * 12
    off_peak_cars = off_peak_intervals * 8

    # Calculate the total number of cars served from 4 pm - 6 pm
    total_cars = peak_cars + off_peak_cars

    result = total_cars
    return result

print(solution())