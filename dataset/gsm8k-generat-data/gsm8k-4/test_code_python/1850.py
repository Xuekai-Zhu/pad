def solution():
    """Drew is reseeding his lawn with grass seed. One bag of grass seed covers 250 square feet of lawn. His lawn is 22 feet from the house to the curb and 36 feet from side to side. He bought four bags of seed. How many extra square feet could the leftover grass seed cover after Drew reseeds his lawn?"""
    # Define the area of Drew's lawn
    lawn_area = 22 * 36

    # Define the area that can be covered by one bag of grass seed
    grass_area = 250

    # Calculate the total area that can be covered by four bags of grass seed
    total_grass_area = grass_area * 4

    # Calculate the leftover grass seed
    leftover_grass_seed = total_grass_area - lawn_area

    # return the result
    result = leftover_grass_seed
    return result

print(solution())