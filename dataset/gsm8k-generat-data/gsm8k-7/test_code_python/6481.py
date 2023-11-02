def solution():
    # Sara's birdhouse dimensions in feet
    sara_width = 1
    sara_height = 2
    sara_depth = 2

    # Jake's birdhouse dimensions in feet
    jake_width = 16 / 12  # convert inches to feet
    jake_height = 20 / 12
    jake_depth = 18 / 12

    # Calculate Sara's birdhouse volume
    sara_volume = sara_width * sara_height * sara_depth

    # Calculate Jake's birdhouse volume
    jake_volume = jake_width * jake_height * jake_depth

    # Calculate the difference in volume between the two birdhouses
    volume_difference = sara_volume - jake_volume
    result = volume_difference
    return result

print(solution())