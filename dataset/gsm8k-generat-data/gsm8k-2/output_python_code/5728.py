def solution():
    """Milly is making feather boas for her dance team. Each flamingo has 20 tail feathers, and it's only safe to pluck 25% of their tail feathers at one time. If Milly needs to make 12 boas, and each boa has 200 feathers, how many flamingoes does she need to harvest?"""
    feathers_per_boa = 200
    boas_needed = 12
    feathers_needed = feathers_per_boa * boas_needed
    feathers_per_flamingo = 20
    safe_feather_removal_percentage = 0.25
    flamingos_needed = feathers_needed / (feathers_per_flamingo * safe_feather_removal_percentage)
    result = flamingos_needed
    return result

print(solution())