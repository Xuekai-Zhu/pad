def solution():
    """John builds a toy bridge to support various weights.  It needs to support 6 cans of soda that have 12 ounces of soda.  The cans weigh 2 ounces empty.  He then also adds 2 more empty cans.  How much weight must the bridge hold up?"""
    # Calculate the weight of one can of soda
    weight_per_can = 12 + 2 # 12 ounces of soda and 2 ounces for the can itself

    # Calculate the weight of the 6 cans of soda
    soda_weight = 6 * weight_per_can

    # Calculate the weight of the 2 empty cans
    empty_can_weight = 2 * 2 # 2 ounces each

    # Calculate the total weight the bridge must hold up
    total_weight = soda_weight + empty_can_weight

    result = total_weight
    return result

print(solution())