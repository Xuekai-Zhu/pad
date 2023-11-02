def solution():
    width = 110
    length = 120
    swath_width = 2
    tilling_speed = 0.5   # in feet per second
    total_area = width * length

    # Calculate the area tilled with each pass
    tilled_area = swath_width * length

    # Calculate the number of passes needed to till the entire plot
    num_passes = int(width / swath_width) + 1

    # Calculate the total time required
    total_time = (num_passes * tilled_area) / tilling_speed

    # Convert time to minutes
    total_time /= 60

    result = total_time
    return result

print(solution())