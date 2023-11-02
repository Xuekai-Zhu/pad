def solution():
    """During the most recent voyage of the Starship Conundrum, the spacecraft traveled from Planet X to Planet Y in eight hours less than twice the number of hours in a typical earth day. If the distance between these two planets is 4,000 parsecs, what was the average speed, in parsecs per hour, of the Starship Conundrum during this most recent voyage?"""
    # Define the distance and time variables
    distance = 4000
    time = 2 * 24 - 8

    # Calculate the average speed and round to two decimal places
    average_speed = distance / time
    result = round(average_speed, 2)
    return result

print(solution())