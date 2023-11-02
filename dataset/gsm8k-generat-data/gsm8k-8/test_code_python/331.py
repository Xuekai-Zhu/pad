def solution():
    # Define constants and variables
    PITCH_PER_TRUCKLOAD = 1
    GRAVEL_PER_TRUCKLOAD = 2 + 5 * PITCH_PER_TRUCKLOAD
    ASPHALT_PER_MILE = 3
    remaining_miles = 16 - 4 - (2 * 4 - 1)  # one mile less than double the first day's paving

    # Calculate the number of truckloads needed for the remaining road
    truckloads_needed = remaining_miles * ASPHALT_PER_MILE

    # Calculate the total amount of pitch and gravel needed for the remaining road
    pitch_needed = truckloads_needed * PITCH_PER_TRUCKLOAD
    gravel_needed = truckloads_needed * GRAVEL_PER_TRUCKLOAD

    # Return the barrels of pitch needed
    return pitch_needed

print(solution())