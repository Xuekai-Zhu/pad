def solution():
    hem_length = 3 * 12  # Convert the hem length from feet to inches
    stitch_length = 1/4  # Jenna makes stitches that are 1/4 inch long
    stitches_per_minute = 24  # Jenna makes 24 stitches per minute

    # Calculate the total number of stitches Jenna needs to make
    total_stitches = hem_length / stitch_length

    # Calculate the time it takes Jenna to make all of the stitches
    time_taken = total_stitches / stitches_per_minute

    result = time_taken
    return result

print(solution())