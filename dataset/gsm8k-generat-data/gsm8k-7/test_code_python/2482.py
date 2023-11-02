def solution():
    hem_length_ft = 3
    stitch_length_inches = 0.25
    stitches_per_minute = 24

    # Convert hem length to inches
    hem_length_inches = hem_length_ft * 12

    # Calculate the total number of stitches needed to hem the dress
    num_stitches = hem_length_inches / stitch_length_inches

    # Calculate the number of minutes it will take to make all the stitches
    num_minutes = num_stitches / stitches_per_minute
    result = num_minutes
    return result

print(solution())