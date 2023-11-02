def solution():
    # Convert hem length to inches
    hem_length_inches = 3 * 12

    # Calculate the total number of stitches needed
    total_stitches = hem_length_inches / 0.25

    # Calculate the number of minutes it will take to make all the stitches
    minutes_to_hem = total_stitches / 24

    result = round(minutes_to_hem, 1)
    return result

print(solution())