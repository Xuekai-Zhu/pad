def solution():
    """Caleb and Cynthia are filling up their inflatable pool with water using buckets. They fill their buckets at the spigot and carry them to the pool. Caleb can add 7 gallons from his bucket and Cynthia can add 8 gallons from her bucket each trip. It will take 105 gallons to fill the pool. How many trips will it take for Caleb and Cynthia to fill the pool with their buckets?"""
    # Define the amount of water each bucket can hold
    CALEB_BUCKET_SIZE = 7
    CYNTHIA_BUCKET_SIZE = 8

    # Define the amount of water needed to fill the pool
    POOL_SIZE = 105

    # Initialize the number of trips for each person
    caleb_trips = 0
    cynthia_trips = 0

    # Fill the pool with buckets
    total_water = 0
    while total_water < POOL_SIZE:
        # Add water from Caleb's bucket
        total_water += CALEB_BUCKET_SIZE
        caleb_trips += 1

        # Add water from Cynthia's bucket
        total_water += CYNTHIA_BUCKET_SIZE
        cynthia_trips += 1

    # Determine who took the last trip and adjust the trips accordingly (since they didn't both contribute to the final amount)
    if total_water - POOL_SIZE == CALEB_BUCKET_SIZE:
        caleb_trips -= 1
    elif total_water - POOL_SIZE == CYNTHIA_BUCKET_SIZE:
        cynthia_trips -= 1

    # Display the total number of trips taken
    result = caleb_trips + cynthia_trips
    return result

print(solution())