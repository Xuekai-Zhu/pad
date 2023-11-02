def solution():
    """Lindsey bought 2 exercise bands to intensify her workout. Each band adds an extra 5 pounds of resistance to her workout. If she doubles up both sets of bands and places them around her legs and picks up a 10-pound dumbbell, how much weight will she squat?"""
    # Define the weight of the dumbbell and the weight added by each band
    dumbbell_weight = 10
    band_weight = 5

    # Double up both sets of bands
    total_band_weight = band_weight * 2

    # Calculate the total weight added
    total_weight_added = total_band_weight + dumbbell_weight

    # The weight Lindsey will squat is equal to the total weight added
    weight_squat = total_weight_added

    result = weight_squat
    return result

print(solution())