def solution():
    """Sara builds a birdhouse that is 1 foot wide, 2 feet tall and 2 feet deep. Jake builds a birdhouse that is 16 inches wide, 20 inches tall and 18 inches deep. What is the difference in volume between the two birdhouses?"""
    # Define the dimensions of Sara's birdhouse in inches
    sara_width = 12
    sara_height = 24
    sara_depth = 24

    # Define the dimensions of Jake's birdhouse in inches
    jake_width = 16
    jake_height = 20
    jake_depth = 18

    # Calculate the volume of Sara's birdhouse in cubic inches
    sara_volume = sara_width * sara_height * sara_depth

    # Calculate the volume of Jake's birdhouse in cubic inches
    jake_volume = jake_width * jake_height * jake_depth

    # Calculate the difference in volume between the two birdhouses
    volume_difference = abs(sara_volume - jake_volume)

    # return the result
    result = volume_difference
    return result

print(solution())