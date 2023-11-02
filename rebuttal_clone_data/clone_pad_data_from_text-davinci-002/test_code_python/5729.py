def solution():
    feathers_needed = 2400
    feathers_per_flamingo = 20
    percent_safe_to_pluck = 25
    safe_amount_to_pluck = feathers_per_flamingo * (percent_safe_to_pluck / 100)
    boas_needed = 12
    feathers_needed = boas_needed * 200
    flamingoes_needed = feathers_needed / safe_amount_to_pluck
    result = flamingoes_needed
    
    return result

print(solution())