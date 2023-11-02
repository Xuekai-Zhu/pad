def solution():
    original_length = 24  # The original length of the fabric is 24 feet
    original_width = 6  # The original width of the fabric is 6 feet

    # Calculate the total area of the fabric
    total_area = original_length * original_width

    # Calculate the length of each side of the square
    side_length = (total_area ** 0.5) / 2

    result = side_length
    return result

print(solution())