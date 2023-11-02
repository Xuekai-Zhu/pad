def solution():
    # Convert Sara's measurements to inches
    sara_width = 12
    sara_height = 24
    sara_depth = 24

    # Calculate Sara's volume
    sara_volume = sara_width * sara_height * sara_depth

    # Calculate Jake's volume
    jake_volume = 16 * 20 * 18

    # Calculate the difference in volume
    volume_difference = sara_volume - jake_volume
    result = volume_difference
    return result

print(solution())