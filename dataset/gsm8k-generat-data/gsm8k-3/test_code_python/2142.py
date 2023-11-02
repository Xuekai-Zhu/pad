def solution():
    """Carson is sorting seaweed for various uses. 50% of the seaweed is only good for starting fires. 25% of what's left can be eaten by humans, and the rest is fed to livestock. If Carson harvests 400 pounds of seaweed, how many pounds are fed to livestock?"""
    # Define the initial percentage of seaweed that can't be used for anything
    unusable_percentage = 0.5

    # Calculate the amount of unusable seaweed
    unusable_seaweed = 400 * unusable_percentage

    # Calculate the amount of usable seaweed
    usable_seaweed = 400 - unusable_seaweed

    # Define the percentage of usable seaweed that can be eaten by humans
    human_percentage = 0.25

    # Calculate the amount of seaweed that can be eaten by humans
    human_seaweed = usable_seaweed * human_percentage

    # Calculate the amount of seaweed that is fed to livestock
    livestock_seaweed = usable_seaweed - human_seaweed

    # Display the amount of seaweed fed to livestock
    result = livestock_seaweed
    return result

print(solution())