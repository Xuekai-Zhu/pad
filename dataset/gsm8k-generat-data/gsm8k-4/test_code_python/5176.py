def solution():
    """
    John builds a toy bridge to support various weights. It needs to support 6 cans of soda that have 12 ounces of soda. 
    The cans weigh 2 ounces empty. He then also adds 2 more empty cans. How much weight must the bridge hold up?
    """
    # Calculate the weight of the 6 cans of soda
    soda_weight = 6 * (12 + 2) # 6 cans with 12 ounces of soda per can and 2 ounces empty weight per can

    # Calculate the weight of the 2 extra empty cans
    extra_cans_weight = 2 * 2 # 2 cans with 2 ounces empty weight per can

    # Calculate the total weight that the bridge must hold up
    total_weight = soda_weight + extra_cans_weight

    # return the result
    result = total_weight
    return result

print(solution())