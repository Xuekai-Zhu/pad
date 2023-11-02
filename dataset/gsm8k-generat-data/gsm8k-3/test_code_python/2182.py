def solution():
    """At peak hours, 11 am - 1 pm and 5 pm - 6 pm, the local fast-food restaurant serves 12 cars every 15 minutes. Off-peak times, they serve 8 cars every 15 minutes. From 4 pm - 6 pm, how many customers do they serve?"""
    # Define the number of cars served during peak hours and off-peak hours
    PEAK_CARS = 12
    OFF_PEAK_CARS = 8

    # Calculate the number of 15-minute intervals during peak hours and off-peak hours
    peak_intervals = (1 - 11) * 4 + (6 - 5) * 4  # 8 intervals total
    off_peak_intervals = (4 - 1) * 4 + (6 - 4) * 4  # 8 intervals total

    # Calculate the number of cars served during peak hours and off-peak hours
    peak_cars_served = peak_intervals * PEAK_CARS
    off_peak_cars_served = off_peak_intervals * OFF_PEAK_CARS

    # Calculate the total number of cars served from 4 pm to 6 pm
    total_cars_served = peak_cars_served + off_peak_cars_served

    # Display the total number of cars served
    result = total_cars_served
    return result

print(solution())