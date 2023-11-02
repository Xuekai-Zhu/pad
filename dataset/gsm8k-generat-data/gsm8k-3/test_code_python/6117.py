def solution():
    """Cape May and Daytona Beach have 40 shark sightings a year. If Cape May has 8 less than double the number of shark sightings of Daytona Beach, how many shark sightings does Cape May have?"""
    # Define the total number of shark sightings
    total_sightings = 40

    # Calculate the number of shark sightings in Daytona Beach
    daytona_sightings = (total_sightings + 8) / 3

    # Calculate the number of shark sightings in Cape May
    cape_may_sightings = 2 * daytona_sightings - 8

    # Display the number of shark sightings in Cape May
    result = cape_may_sightings
    return result

print(solution())