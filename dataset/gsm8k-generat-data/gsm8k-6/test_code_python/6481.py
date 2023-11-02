def solution():
    # Calculate the volume of Sara's birdhouse
    sara_volume = 1 * 2 * 2  # volume = length x width x height (in feet)

    # Calculate the volume of Jake's birdhouse (converting inches to feet)
    jake_volume = (16/12) * (20/12) * (18/12)

    # Calculate the difference in volume between the two birdhouses
    volume_difference = sara_volume - jake_volume
    result = volume_difference
    return result

print(solution())