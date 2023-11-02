def solution():
    total_seaweed = 400
    fire_seaweed = total_seaweed * 0.5  # 50% for starting fires
    edible_seaweed = (total_seaweed - fire_seaweed) * 0.25  # 25% of what's left can be eaten
    livestock_seaweed = total_seaweed - fire_seaweed - edible_seaweed  # the rest is fed to livestock
    result = livestock_seaweed
    return result

print(solution())