def solution():
    """Caleb and Cynthia are filling up their inflatable pool with water using buckets. They fill their buckets at the spigot and carry them to the pool. Caleb can add 7 gallons from his bucket and Cynthia can add 8 gallons from her bucket each trip. It will take 105 gallons to fill the pool. How many trips will it take for Caleb and Cynthia to fill the pool with their buckets?"""
    # Define the amount of water each bucket can hold
    caleb_bucket = 7
    cynthia_bucket = 8

    # Define the total amount of water needed to fill the pool
    total_water = 105

    # Initialize the number of trips counter for Caleb and Cynthia
    caleb_trips = 0
    cynthia_trips = 0

    # Initialize the total amount of water added to the pool
    water_added = 0

    # Fill the pool using the buckets until the total amount of water added equals the total amount of water needed
    while water_added < total_water:
        # Increment the trip counters for Caleb and Cynthia
        caleb_trips += 1
        cynthia_trips += 1

        # Add the amount of water from each bucket to the pool
        water_added += caleb_bucket + cynthia_bucket

    # Display the number of trips needed to fill the pool
    result = caleb_trips + cynthia_trips
    return result

print(solution())