def solution():
    # Calculate the distance around the lake
    distance = 15 * 4  # Each side of the lake is 15 miles, so the distance around is 4*15 = 60 miles

    # Calculate John's swimming speed and rowing speed
    swimming_speed = 1 / (20/60)  # Jake swims 1 mile in 20 minutes, so his swimming speed is 1/(20/60) miles per hour
    rowing_speed = 2 * swimming_speed  # Jake's rowing speed is twice his swimming speed

    # Calculate the time it takes to row around the lake
    time = distance / rowing_speed  # Time = Distance / Speed

    # Convert the time from hours to minutes
    time = time * 60

    result = time
    return result

print(solution())