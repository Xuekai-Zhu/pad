def solution():
    # Define how many times Malcolm brushes his teeth per day
    brushes_per_day = 3

    # Define how long Malcolm brushes his teeth each time
    brush_length = 2  # in minutes

    # Calculate how many minutes Malcolm brushes his teeth per day
    minutes_per_day = brushes_per_day * brush_length

    # Calculate how many minutes Malcolm brushes his teeth after 30 days
    total_minutes = minutes_per_day * 30

    # Convert total_minutes to hours
    hours = total_minutes / 60

    result = hours
    return result

print(solution())