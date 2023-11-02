def solution():
    
    seabed_to_base = 300
    seabed_to_peak = seabed_to_base / 0.25
    hill_height = seabed_to_peak - seabed_to_base
    result = hill_height
    return result

print(solution())