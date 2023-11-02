def solution():
    # original number of seeds
    total_seeds = 23

    # number of seeds that didn't grow
    non_growing_seeds = 5

    # remaining seeds
    remaining_seeds = total_seeds - non_growing_seeds

    # number of seeds that grew but were eaten
    eaten_plants = remaining_seeds / 3

    # number of uneaten plants left
    uneaten_plants = remaining_seeds - eaten_plants

    # number of plants strangled by weeds
    strangled_plants = uneaten_plants / 3

    # number of plants remaining after removing weeds and strangled plants
    remaining_plants = uneaten_plants - strangled_plants - 2 + 1

    result = remaining_plants
    return result

print(solution())