def solution():
    """Lindsey bought 2 exercise bands to intensify her workout. Each band adds an extra 5 pounds of resistance to her workout. If she doubles up both sets of bands and places them around her legs and picks up a 10-pound dumbbell, how much weight will she squat?"""
    band_weight = 5
    num_bands = 2
    total_band_weight = band_weight * num_bands * 2
    dumbbell_weight = 10
    total_weight = total_band_weight + dumbbell_weight
    result = total_weight
    return result

print(solution())