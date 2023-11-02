def solution():
    # Calculate the total length of string in inches
    total_length = 15 * 12  # 15 feet = 180 inches

    # Calculate the number of 6-inch wicks Amy will cut
    num_6inch = total_length // 6

    # Calculate the number of 12-inch wicks Amy will cut
    num_12inch = total_length // 12

    # Calculate the total number of wicks Amy will cut
    total_wicks = num_6inch + num_12inch

    result = total_wicks
    return result

print(solution())