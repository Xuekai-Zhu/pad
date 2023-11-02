def solution():
    human_lifespan = 79
    monkey_lifespan = 48   # Choose the average of the longest-lived monkey species
    if monkey_lifespan > human_lifespan:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())