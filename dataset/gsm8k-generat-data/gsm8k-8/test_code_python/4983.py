def solution():
    # Calculate the total water needed for both Violet and her dog per hour
    total_water_per_hour = 800 + 400

    # Calculate the total water needed for both Violet and her dog for the entire hike
    total_water_needed = total_water_per_hour * hours

    # Convert the total water needed to liters
    total_water_needed_liters = total_water_needed / 1000

    # Calculate the number of hours Violet and her dog can hike with the amount of water she can carry
    hours = 4.8 / total_water_needed_liters
    result = hours
    return result

print(solution())