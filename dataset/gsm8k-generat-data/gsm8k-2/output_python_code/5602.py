def solution():
    """James supercharges his car which increases his car's speed by 30%. He then cuts weight by 15% which increases the speed a further 10 mph. If his car's original speed was 150 mph what is the new speed?"""
    original_speed = 150
    supercharge_percent = 0.3
    weight_cut_percent = 0.15
    supercharged_speed = original_speed * (1 + supercharge_percent)
    weight_cut_speed = supercharged_speed + 10
    final_speed = weight_cut_speed / (1 - weight_cut_percent)
    result = final_speed
    return result

print(solution())