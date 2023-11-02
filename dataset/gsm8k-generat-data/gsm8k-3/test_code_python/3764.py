def solution():
    """Lindsey bought 2 exercise bands to intensify her workout.  Each band adds an extra 5 pounds of resistance to her workout.  If she doubles up both sets of bands and places them around her legs and picks up a 10-pound dumbbell, how much weight will she squat?"""
    # Define the weight added by each exercise band
    BAND_WEIGHT = 5

    # Calculate the total weight added by both sets of bands
    band_weight_total = 2 * BAND_WEIGHT

    # Calculate the total weight of the squat
    squat_weight = band_weight_total + 10

    # Display the total weight of the squat
    result = squat_weight
    return result

print(solution())