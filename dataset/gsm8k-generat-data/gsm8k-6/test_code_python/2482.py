def solution():
    # Convert hem length to inches
    hem_length = 3 * 12  # 1 foot = 12 inches

    # Calculate the number of stitches needed to hem the dress
    num_stitches = hem_length / (1/4)

    # Calculate the time in minutes to make 24 stitches
    time_per_24_stitches = 24 / 60  # 24 stitches per minute

    # Calculate the total time in minutes to hem the dress
    total_time = num_stitches * time_per_24_stitches

    result = total_time
    return result

print(solution())