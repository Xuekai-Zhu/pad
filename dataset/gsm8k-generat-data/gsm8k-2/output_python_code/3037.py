def solution():
    """During the most recent voyage of the Starship Conundrum, the spacecraft traveled from Planet X to Planet Y in eight hours less
    than twice the number of hours in a typical earth day. If the distance between these two planets is 4,000 parsecs, what was the average
    speed, in parsecs per hour, of the Starship Conundrum during this most recent voyage?"""
    typical_earth_day_hours = 24
    voyage_hours = 2 * typical_earth_day_hours - 8
    distance = 4000
    speed = distance / voyage_hours
    result = speed
    return result

print(solution())