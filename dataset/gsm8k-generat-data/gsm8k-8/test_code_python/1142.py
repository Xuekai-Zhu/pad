def solution():
    # Define the number of shark sightings in Daytona Beach
    daytona_sightings = 26
    
    # Calculate the number of shark sightings in Cape May
    cape_may_sightings = (daytona_sightings - 5) / 3
    
    result = cape_may_sightings
    return result

print(solution())