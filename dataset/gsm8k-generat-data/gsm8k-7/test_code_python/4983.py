def solution():
    violet_water_per_hour = 800
    dog_water_per_hour = 400
    total_water_per_hour = violet_water_per_hour + dog_water_per_hour
    total_water_capacity = 4.8 * 1000  # convert liters to ml

    # Calculate the total number of hours they can spend hiking
    total_hours = total_water_capacity / total_water_per_hour
    result = total_hours
    return result

print(solution())