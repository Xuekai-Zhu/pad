def solution():
    """Milly is making feather boas for her dance team. Each flamingo has 20 tail feathers, and it's only safe to pluck 25% of their tail feathers at one time. If Milly needs to make 12 boas, and each boa has 200 feathers, how many flamingoes does she need to harvest?"""
    feathers_per_flamingo = 20
    safe_percent = 0.25
    feathers_per_harvest = feathers_per_flamingo * safe_percent
    boas_needed = 12
    feathers_per_boa = 200
    total_feathers_needed = boas_needed * feathers_per_boa
    flamingos_needed = total_feathers_needed / feathers_per_harvest
    result = flamingos_needed
    return result

print(solution())