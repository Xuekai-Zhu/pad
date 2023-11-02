def solution():
    """Carson is sorting seaweed for various uses. 50% of the seaweed is only good for starting fires. 25% of what's left can be eaten by humans, and the rest is fed to livestock. If Carson harvests 400 pounds of seaweed, how many pounds are fed to livestock?"""
    # Define the total weight of harvested seaweed
    total_weight = 400

    # Calculate the weight of seaweed only good for starting fires
    fire_weight = total_weight * 0.5

    # Calculate the weight of seaweed left for other uses
    remaining_weight = total_weight - fire_weight

    # Calculate the weight of seaweed that can be eaten by humans
    human_weight = remaining_weight * 0.25

    # Calculate the weight of seaweed fed to livestock
    livestock_weight = remaining_weight - human_weight

    # return the result
    result = livestock_weight
    return result

print(solution())