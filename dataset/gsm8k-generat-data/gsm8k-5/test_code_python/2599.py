def solution():
    total_length = 15 * 12  # Convert 15 feet to 180 inches
    short_wick_length = 6  # Each short wick is 6 inches long
    long_wick_length = 12  # Each long wick is 12 inches long

    # Calculate the number of short wicks
    num_short_wicks = total_length // short_wick_length

    # Calculate the number of long wicks
    num_long_wicks = total_length // long_wick_length

    # Calculate the total number of wicks
    total_num_wicks = num_short_wicks + num_long_wicks
    result = total_num_wicks
    return result

print(solution())