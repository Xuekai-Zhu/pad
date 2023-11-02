def solution():
    # Calculate the number of animal sightings in February
    february_sightings = 3 * 26

    # Calculate the number of animal sightings in March
    march_sightings = february_sightings / 2

    # Calculate the total number of animal sightings in the first three months
    total_sightings = 26 + february_sightings + march_sightings
    result = total_sightings
    return result

print(solution())