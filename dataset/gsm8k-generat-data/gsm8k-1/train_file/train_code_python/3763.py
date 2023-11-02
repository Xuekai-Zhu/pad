def solution():
    """Lindsey bought 2 exercise bands to intensify her workout. Each band adds an extra 5 pounds of resistance to her workout. If she doubles up both sets of bands and places them around her legs and picks up a 10-pound dumbbell, how much weight will she squat?"""
    extra_weight_per_band = 5
    total_extra_weight = extra_weight_per_band * 2
    dumbbell_weight = 10
    total_weight = (dumbbell_weight + total_extra_weight) * 2
    result = total_weight
    return result

print(solution())