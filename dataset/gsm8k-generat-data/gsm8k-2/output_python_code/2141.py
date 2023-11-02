def solution():
    """Carson is sorting seaweed for various uses. 50% of the seaweed is only good for starting fires. 25% of what's left can be eaten by humans, and the rest is fed to livestock. If Carson harvests 400 pounds of seaweed, how many pounds are fed to livestock?"""
    seaweed = 400
    fire_seaweed = 0.5 * seaweed
    edible_seaweed = 0.25 * (seaweed - fire_seaweed)
    livestock_seaweed = seaweed - fire_seaweed - edible_seaweed
    result = livestock_seaweed
    return result

print(solution())