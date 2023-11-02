def solution():
    num_lake_races = 5  # Half of the races were in a lake
    num_ocean_races = 5  # Half of the races were in an ocean
    race_distance = 3  # Each race was 3 miles long
    lake_speed = 3  # Tyson can swim 3 miles per hour in a lake
    ocean_speed = 2.5  # Tyson can swim 2.5 miles per hour in an ocean

    # Calculate the time it takes for Tyson to complete a lake race
    lake_time = race_distance / lake_speed

    # Calculate the time it takes for Tyson to complete an ocean race
    ocean_time = race_distance / ocean_speed

    # Calculate the total time Tyson spent racing
    total_time = (num_lake_races * lake_time) + (num_ocean_races * ocean_time)
    result = total_time
    return result

print(solution())