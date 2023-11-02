def solution():
    # Calculate the distance of the first half of the journey
    distance_first_half = (28/60) * 0.5  # driving 28 mph for half an hour
    # Calculate the distance of the second half of the journey
    distance_second_half = (60/60) * 0.5  # driving 60 mph for half an hour
    total_distance = distance_first_half + distance_second_half

    # Calculate the time it will take Jake to bike to the water park
    time = total_distance / 11
    result = time
    return result

print(solution())