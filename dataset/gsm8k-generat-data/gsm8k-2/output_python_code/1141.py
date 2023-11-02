def solution():
    """Daytona Beach has 26 shark sightings a year. Daytona Beach has 5 more than triple the number of shark sightings as Cape May. How many shark sightings are there in Cape May?"""
    daytona_sightings = 26
    cape_may_sightings = (daytona_sightings - 5) / 3
    result = cape_may_sightings
    return result

print(solution())