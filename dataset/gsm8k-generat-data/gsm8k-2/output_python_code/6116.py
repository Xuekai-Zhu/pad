def solution():
    """Cape May and Daytona Beach have 40 shark sightings a year. If Cape May has 8 less than double the number of shark sightings of Daytona Beach, how many shark sightings does Cape May have?"""
    total_sightings = 40
    db_sightings = (total_sightings / 3) * 2
    cm_sightings = (2 * db_sightings) - 8
    result = cm_sightings
    return result

print(solution())