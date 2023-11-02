def solution():
    """Caleb and Cynthia are filling up their inflatable pool with water using buckets. They fill their buckets at the spigot and carry them to the pool. Caleb can add 7 gallons from his bucket and Cynthia can add 8 gallons from her bucket each trip. It will take 105 gallons to fill the pool. How many trips will it take for Caleb and Cynthia to fill the pool with their buckets?"""
    caleb_bucket = 7
    cynthia_bucket = 8
    pool_capacity = 105
    combined_capacity = caleb_bucket + cynthia_bucket
    trips_needed = pool_capacity // combined_capacity
    if pool_capacity % combined_capacity > 0:
        trips_needed += 1
    result = trips_needed
    return result

print(solution())