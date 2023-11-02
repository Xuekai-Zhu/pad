def solution():
    # Calculate the area of Drew's lawn
    lawn_area = 22 * 36

    # Calculate the total area covered by the grass seed
    seed_area = 250 * 4

    # Calculate the extra square feet the leftover grass seed can cover
    extra_area = seed_area - lawn_area

    result = extra_area
    return result

print(solution())