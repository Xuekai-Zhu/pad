def solution():
    own_packs = 3
    neighbor_packs = 2
    balloons_per_pack = 6
    extra_balloons = 7

    # Calculate the total number of water balloons
    total_balloons = (own_packs + neighbor_packs) * balloons_per_pack

    # Calculate the number of balloons each person gets
    balloons_per_person = total_balloons / 2

    # Calculate the number of balloons Floretta is left with
    floretta_balloons = balloons_per_person - extra_balloons

    result = floretta_balloons
    return result

print(solution())