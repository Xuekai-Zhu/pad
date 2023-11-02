def solution():
    total_sightings = 40
    db_sightings = (total_sightings + 8) / 2  # get the number of shark sightings in Daytona Beach
    cm_sightings = 2 * db_sightings - 8  # calculate the number of shark sightings in Cape May
    result = cm_sightings
    return result

print(solution())