def solution():
    # Calculate the number of seeds that survive after 1/3rd are lost in water
    surviving_seeds = (2/3) * 300

    # Calculate the number of seeds that survive after 1/6th are eaten by insects
    surviving_seeds = surviving_seeds - (1/6) * 300

    # Calculate the number of seeds that sprout and are immediately eaten
    surviving_seeds = (1/2) * (surviving_seeds - (1/2) * surviving_seeds)

    # Calculate the number of dandelions that survive long enough to flower
    surviving_dandelions = surviving_seeds / 300

    result = surviving_dandelions
    return result

print(solution())