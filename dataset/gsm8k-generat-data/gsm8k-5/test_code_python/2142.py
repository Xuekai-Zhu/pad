def solution():
    seaweed_for_fire = 0.5 * 400  # 50% of seaweed is only good for starting fires
    seaweed_left = 400 - seaweed_for_fire  # Subtract the seaweed used for starting fires

    seaweed_for_humans = 0.25 * seaweed_left  # 25% of the remaining seaweed can be eaten by humans
    seaweed_for_livestock = seaweed_left - seaweed_for_humans  # The rest of the remaining seaweed is fed to livestock

    result = seaweed_for_livestock
    return result

print(solution())