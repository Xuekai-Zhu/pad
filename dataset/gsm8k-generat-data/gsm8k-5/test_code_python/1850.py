def solution():
    # Calculate the area of the lawn
    lawn_area = 22 * 36  # The lawn is 22 feet from the house to the curb and 36 feet from side to side

    # Calculate the total area covered by the grass seed
    total_grass_area = 4 * 250  # Drew bought four bags of grass seed, and each bag covers 250 square feet

    # Calculate the extra square feet that the leftover grass seed can cover
    extra_grass_area = total_grass_area - lawn_area

    result = extra_grass_area
    return result

print(solution())