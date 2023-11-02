def solution():
    # Calculate the pounds of seaweed fed to livestock
    starting_fire = 0.5 * 400
    remaining = 400 - starting_fire
    human_consumption = 0.25 * remaining
    livestock_consumption = remaining - human_consumption
    result = livestock_consumption
    return result

print(solution())