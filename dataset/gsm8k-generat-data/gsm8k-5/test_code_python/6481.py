def solution():
    # Convert Sara's dimensions to inches
    sara_width = 12  # 1 foot is equal to 12 inches
    sara_height = 24  # 2 feet is equal to 24 inches
    sara_depth = 24  # 2 feet is equal to 24 inches

    # Calculate Sara's volume
    sara_volume = sara_width * sara_height * sara_depth

    # Convert Jake's dimensions to inches
    jake_width = 16
    jake_height = 20
    jake_depth = 18

    # Calculate Jake's volume
    jake_volume = jake_width * jake_height * jake_depth

    # Calculate the difference in volume
    volume_difference = (sara_volume - jake_volume) / (12 ** 3)  # Convert back to cubic feet
    result = volume_difference
    return result

print(solution())