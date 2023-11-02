def solution():
    """Cape May and Daytona Beach have 40 shark sightings a year. If Cape May has 8 less than double the number of shark sightings of Daytona Beach, how many shark sightings does Cape May have?"""
    # Define the total shark sightings
    total_sightings = 40

    # Calculate the number of shark sightings at Daytona Beach
    daytona_sightings = total_sightings / 3

    # Calculate the number of shark sightings at Cape May
    cape_may_sightings = 2 * daytona_sightings - 8

    # return the result
    result = cape_may_sightings
    return result

print(solution())