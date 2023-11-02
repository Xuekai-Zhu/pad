def solution():
    """Drew is reseeding his lawn with grass seed. One bag of grass seed covers 250 square feet of lawn. His lawn is 22 feet from the house to the curb and 36 feet from side to side. He bought four bags of seed. How many extra square feet could the leftover grass seed cover after Drew reseeds his lawn?"""
    # Define the area of Drew's lawn
    lawn_area = 22 * 36

    # Define the area covered by one bag of grass seed
    seed_area = 250

    # Calculate the total area covered by the four bags of seed
    total_seed_area = seed_area * 4

    # Calculate the extra square feet that the leftover grass seed could cover
    extra_area = total_seed_area - lawn_area

    # Display the extra square feet
    result = extra_area
    return result

print(solution())