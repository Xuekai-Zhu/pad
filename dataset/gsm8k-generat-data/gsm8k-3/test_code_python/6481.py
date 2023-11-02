def solution():
    """Sara builds a birdhouse that is 1 foot wide, 2 feet tall and 2 feet deep. Jake builds a birdhouse that is 16 inches wide, 20 inches tall and 18 inches deep. What is the difference in volume between the two birdhouses?"""
    # Calculate the volume of Sara's birdhouse in cubic feet
    sara_width = 1  # width in feet
    sara_height = 2  # height in feet
    sara_depth = 2  # depth in feet
    sara_volume = sara_width * sara_height * sara_depth

    # Calculate the volume of Jake's birdhouse in cubic feet
    jake_width = 16 / 12  # convert width to feet
    jake_height = 20 / 12  # convert height to feet
    jake_depth = 18 / 12  # convert depth to feet
    jake_volume = jake_width * jake_height * jake_depth

    # Calculate the difference in volume between the two birdhouses
    difference = sara_volume - jake_volume

    # Display the difference in volume
    result = difference
    return result

print(solution())