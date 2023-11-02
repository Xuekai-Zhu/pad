def solution():
    """During the most recent voyage of the Starship Conundrum, the spacecraft traveled from Planet X to Planet Y in eight hours less than twice the number of hours in a typical earth day.  If the distance between these two planets is 4,000 parsecs, what was the average speed, in parsecs per hour, of the Starship Conundrum during this most recent voyage?"""
    # Define the typical number of hours in an earth day
    EARTH_DAY_HOURS = 24

    # Calculate the number of hours for the recent voyage
    voyage_hours = 2 * EARTH_DAY_HOURS - 8

    # Calculate the average speed
    distance = 4000 # parsecs
    average_speed = distance / voyage_hours

    # Display the average speed
    result = average_speed
    return result.

print(solution())