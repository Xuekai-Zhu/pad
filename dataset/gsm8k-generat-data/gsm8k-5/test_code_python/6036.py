def solution():
    tank_height = 18  # The fish tank is 18 inches tall
    rain_collected = 0  # Initialize the rain collected in the fish tank to 0 inches

    # Calculate the rain collected in the first hour
    rain_collected += 2

    # Calculate the rain collected in the next four hours
    rain_collected += 4 * 1

    # Calculate the time it takes to fill the remaining height of the fish tank
    remaining_height = tank_height - rain_collected
    time_remaining = remaining_height / 3

    # Calculate the total time it takes to fill the fish tank
    total_time = 1 + 4 + time_remaining

    # Convert the total time to hours and minutes
    hours = int(total_time)
    minutes = int((total_time - hours) * 60)

    # Format the time as a string
    time_str = f"{hours}:{minutes:02d}"

    result = time_str
    return result

print(solution())