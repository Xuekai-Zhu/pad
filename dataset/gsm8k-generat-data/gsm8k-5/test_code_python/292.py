def solution():
    scarves_per_yarn = 3  # May can knit 3 scarves using one yarn
    red_yarns = 2
    blue_yarns = 6
    yellow_yarns = 4

    # Calculate the total number of scarves May can make
    total_scarves = (scarves_per_yarn * red_yarns) + (scarves_per_yarn * blue_yarns) + (scarves_per_yarn * yellow_yarns)
    result = total_scarves
    return result

print(solution())