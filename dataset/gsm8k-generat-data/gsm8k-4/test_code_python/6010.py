def solution():
    """James can do a farmer's walk with 300 pounds per hand for 20 meters. 
    He can lift 30% more if he only goes 10 meters. In addition, lifting 
    straps give him another 20%. How much can he move with lifting straps 
    for 10 meters if he increases his 20-meter distance without straps by 
    50 pounds and everything else increases in proportion?"""
    
    # Define initial variables
    weight_20_meters = 300
    distance_20_meters = 20
    distance_10_meters = 10
    additional_weight = 50
    shorter_distance_multiplier = 1.3
    lifting_straps_multiplier = 1.2

    # Calculate the new weight with the added 50 pounds
    new_weight_20_meters = weight_20_meters + additional_weight

    # Calculate the weight James can lift for 10 meters without lifting straps
    weight_10_meters = new_weight_20_meters * shorter_distance_multiplier

    # Calculate the weight James can lift for 10 meters with lifting straps
    weight_with_straps = weight_10_meters * lifting_straps_multiplier

    result = weight_with_straps
    return result

print(solution())