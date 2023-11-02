def solution():
    # Calculate the amount of seaweed only good for starting fires
    fire_seaweed = 0.5 * 400

    # Calculate the amount of seaweed that can be eaten by humans
    human_seaweed = 0.25 * (400 - fire_seaweed)

    # Calculate the amount of seaweed that is fed to livestock
    livestock_seaweed = 400 - fire_seaweed - human_seaweed
    result = livestock_seaweed
    return result

print(solution())