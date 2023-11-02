def solution():
    """James can do a farmer's walk with 300 pounds per hand for 20 meters. He can lift 30% more if he only goes 10 meters. In addition, lifting straps give him another 20%. How much can he move with lifting straps for 10 meters if he increases his 20-meter distance without straps by 50 pounds and everything else increases in proportion?"""
    weight_per_hand = 300
    distance_20m = 20
    distance_10m = 10
    lift_increase = 0.3
    strap_increase = 0.2
    weight_increase = 50
    increased_weight_per_hand = weight_per_hand + weight_increase
    increased_weight_20m = increased_weight_per_hand * distance_20m
    increased_weight_10m = (weight_per_hand * (1 + lift_increase)) * distance_10m
    weight_with_straps = increased_weight_10m * (1 + strap_increase)
    result = weight_with_straps
    return result

print(solution())