def solution():
    weight = 300
    distance_long = 20
    distance_short = 10
    increase = 0.3
    strap_increase = 0.2
    distance_long_weight = weight * (1 + increase)
    distance_short_weight = distance_long_weight * (distance_short/distance_long)
    strap_weight = distance_short_weight * (1 + strap_increase)
    result = strap_weight + 50
    return result

print(solution())