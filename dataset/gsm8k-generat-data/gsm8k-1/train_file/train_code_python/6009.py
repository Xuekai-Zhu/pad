def solution():
    """James can do a farmer's walk with 300 pounds per hand for 20 meters. He can lift 30% more if he only goes 10 meters. In addition, lifting straps give him another 20%. How much can he move with lifting straps for 10 meters if he increases his 20-meter distance without straps by 50 pounds and everything else increases in proportion?"""
    weight_per_hand = 300
    distance_20m = 20
    distance_10m = 10
    increase_percent = 30
    straps_increase_percent = 20
    
    # Calculation for 20m without straps
    increased_weight = weight_per_hand + 50
    weight_20m = increased_weight * distance_20m
    
    # Calculation for 10m without straps
    weight_10m = (weight_per_hand * (1 + increase_percent/100)) * distance_10m
    
    # Calculation for 10m with straps
    weight_10m_straps = weight_10m * (1 + straps_increase_percent/100)
    
    result = weight_10m_straps
    return result

print(solution())