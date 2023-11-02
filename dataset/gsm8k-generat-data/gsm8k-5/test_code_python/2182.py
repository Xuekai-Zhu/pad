def solution():
    peak_hour_cars = 12  # The restaurant serves 12 cars every 15 minutes during peak hours
    off_peak_cars = 8  # The restaurant serves 8 cars every 15 minutes during off-peak hours
    peak_hours = 2  # The peak hours are from 5 pm - 6 pm, and there are two peak hours
    off_peak_hours = 2  # The off-peak hours are from 4 pm - 5 pm, and there are two off-peak hours

    # Calculate the number of cars served during peak hours
    peak_hours_cars = peak_hour_cars * (peak_hours * 4)  # There are 4 sets of 15-minute intervals in each hour

    # Calculate the number of cars served during off-peak hours
    off_peak_hours_cars = off_peak_cars * (off_peak_hours * 4)  # There are 4 sets of 15-minute intervals in each hour

    # Calculate the total number of cars served from 4 pm - 6 pm
    total_cars_served = peak_hours_cars + off_peak_hours_cars
    result = total_cars_served
    return result

print(solution())