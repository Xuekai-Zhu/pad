def solution():
    num_dogs = 5

    # First dog carried off 3 bones
    total_bones = 3

    # Second dog carried off 1 less bone than the first dog
    total_bones += (3 - 1)

    # Third dog carried off twice as many as the second dog
    total_bones += ((3 - 1) * 2)

    # Fourth dog carried off one bone
    total_bones += 1

    # Fifth dog carried off twice as many as the fourth dog carried
    total_bones += (1 * 2)

    result = total_bones
    return result

print(solution())