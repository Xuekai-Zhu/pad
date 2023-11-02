def solution():
    
    feathers_per_boa = 200
    boas_needed = 12
    feathers_needed = feathers_per_boa * boas_needed
    feathers_per_flamingo = 20
    safe_feather_removal_percentage = 0.25
    flamingos_needed = feathers_needed / (feathers_per_flamingo * safe_feather_removal_percentage)
    result = flamingos_needed
    return result

print(solution())