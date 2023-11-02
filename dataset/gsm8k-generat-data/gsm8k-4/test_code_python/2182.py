def solution():
    """At peak hours, 11 am - 1 pm and 5 pm - 6 pm, the local fast-food restaurant serves 12 cars every 15 minutes. Off-peak times, they serve 8 cars every 15 minutes. From 4 pm - 6 pm, how many customers do they serve?"""
    # Define the number of cars served during peak hours and off-peak hours
    peak_cars = 12
    off_peak_cars = 8

    # Calculate the number of cars served during the first hour (4 pm - 5 pm)
    first_hour_cars = off_peak_cars * 4

    # Calculate the number of cars served during the second hour (5 pm - 6 pm)
    second_hour_cars = peak_cars * 4 + off_peak_cars * 3

    # Calculate the total number of cars served during both hours
    total_cars = first_hour_cars + second_hour_cars

    # return the result
    result = total_cars
    return result

print(solution())