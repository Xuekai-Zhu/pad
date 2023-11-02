def solution():
    # Define the number of hours in an earth day
    earth_day = 24

    # Calculate the number of hours for the voyage from Planet X to Planet Y
    voyage_hours = 2 * earth_day - 8

    # Calculate the average speed of the Starship Conundrum during the voyage
    avg_speed = 4000 / voyage_hours
    result = avg_speed
    return result

print(solution())