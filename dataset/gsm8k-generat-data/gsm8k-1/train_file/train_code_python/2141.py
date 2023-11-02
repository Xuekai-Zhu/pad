def solution():
    """Carson is sorting seaweed for various uses. 50% of the seaweed is only good for starting fires. 25% of what's left can be eaten by humans, and the rest is fed to livestock. If Carson harvests 400 pounds of seaweed, how many pounds are fed to livestock?"""
    seaweed_harvested = 400
    fire_seaweed = seaweed_harvested * 0.5
    remaining_seaweed = seaweed_harvested - fire_seaweed
    human_eatable_seaweed = remaining_seaweed * 0.25
    livestock_seaweed = remaining_seaweed - human_eatable_seaweed
    result = livestock_seaweed
    return result

print(solution())