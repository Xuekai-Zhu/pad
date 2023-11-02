def solution():
    """John builds a toy bridge to support various weights. It needs to support 6 cans of soda that have 12 ounces of soda. The cans weigh 2 ounces empty. He then also adds 2 more empty cans. How much weight must the bridge hold up?"""
    weight_per_can = 14  # 12 oz of soda + 2 oz empty can
    total_cans = 6 + 2  # 6 cans of soda + 2 empty cans
    total_weight = weight_per_can * total_cans
    result = total_weight
    return result

print(solution())