def solution():
    total_length = 15  # length of string in feet
    length_6in_wick = 0.5  # length of 6-inch wick in feet
    length_12in_wick = 1  # length of 12-inch wick in feet

    # Calculate the number of 6-inch wicks Amy can get from the string
    num_6in_wicks = (total_length / length_6in_wick) / 2

    # Calculate the number of 12-inch wicks Amy can get from the string
    num_12in_wicks = (total_length / length_12in_wick) / 2

    # Calculate the total number of wicks
    total_num_wicks = num_6in_wicks + num_12in_wicks
    result = total_num_wicks
    return result

print(solution())