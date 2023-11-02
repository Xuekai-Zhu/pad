def solution():
    typical_hours_per_day = 24  # Typical hours in an Earth day
    travel_time = (2 * typical_hours_per_day) - 8  # Travel time in hours from Planet X to Planet Y
    distance = 4000  # Distance between Planet X and Planet Y in parsecs

    # Calculate the average speed of the Starship Conundrum during the voyage
    average_speed = distance / travel_time
    result = average_speed
    return result

print(solution())