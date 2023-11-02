def solution():
    # Number of animals in the initial group
    initial_group = 1  # 1 dog

    # Number of animals after the cats join
    cats = 4
    after_cats = initial_group + cats  # 1 dog + 4 cats

    # Number of animals after the rabbits join
    rabbits = 2 * cats  # 2 rabbits for each cat
    after_rabbits = after_cats + rabbits  # 1 dog + 4 cats + 8 rabbits

    # Number of animals after the hares join
    hares = 3 * rabbits  # 3 hares for each rabbit
    total_animals = after_rabbits + hares  # 1 dog + 4 cats + 8 rabbits + 24 hares
    result = total_animals
    return result

print(solution())