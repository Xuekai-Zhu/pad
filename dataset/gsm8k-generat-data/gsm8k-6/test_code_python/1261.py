def solution():
    # Calculate the number of cakes that were knocked over by the crow
    knocked_over_cakes = 12 / 2  # half of the stack was knocked over by the crow

    # Calculate the number of cakes that remained on the stack
    remaining_cakes = 12 - knocked_over_cakes

    # Calculate the number of cakes that were destroyed
    destroyed_cakes = knocked_over_cakes / 2  # half of the knocked over cakes were destroyed

    result = destroyed_cakes
    return result

print(solution())