def solution():
    """Tom's puts 30 miles per day on his bike for the first 183 days of the year. For the rest of the days of the year he goes 35 miles per day. How many miles does he drive for the year?"""
    # Define the number of days for each distance
    bike_days = 183
    car_days = 365 - bike_days

    # Calculate the total distance for biking
    bike_distance = bike_days * 30

    # Calculate the total distance for driving
    car_distance = car_days * 35

    # Calculate the total distance for the year
    total_distance = bike_distance + car_distance

    # Return the result
    result = total_distance
    return result

print(solution())