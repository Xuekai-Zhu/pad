def solution():
    # Define the total number of shark sightings
    total_sightings = 40

    # Calculate the number of shark sightings in Daytona Beach
    daytona_sightings = total_sightings / 2

    # Calculate the number of shark sightings in Cape May
    cape_may_sightings = daytona_sightings - 8

    result = cape_may_sightings
    return result

print(solution())