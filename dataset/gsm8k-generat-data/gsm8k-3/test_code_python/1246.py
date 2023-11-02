def solution():
    """
    A spaceship is traveling to another planet. The spaceship travels at a consistent speed its entire journey
    unless it is stopped for the crew’s break. After launch, the spaceship traveled for 10 hours then stopped for 3 hours.
    It then traveled for another 10 hours then stopped for 1 hour. After this, the spaceship would take an hour’s break after
    every 11 hours of traveling and maintained this routine until the end of its journey. If the entire journey took 3 days
    then how long, in hours, was the spaceship not moving?
    """
    # Calculate the total number of hours in 3 days
    total_hours = 3 * 24

    # Calculate the total number of hours the spaceship traveled without breaks
    without_breaks = (10 + 10) + ((total_hours - 24) // 11) * (10 + 1)

    # Calculate the total number of hours the spaceship spent on breaks
    on_breaks = 3 + 1 + ((total_hours - 24) // 11)

    # Calculate the total number of hours the spaceship was not moving
    not_moving = total_hours - without_breaks - on_breaks

    # Display the total number of hours the spaceship was not moving
    result = not_moving
    return result

print(solution())