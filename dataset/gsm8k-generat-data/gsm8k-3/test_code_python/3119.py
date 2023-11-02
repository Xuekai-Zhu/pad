def solution():
    """Nick has 60 cans. Each can takes up 30 square inches of space before being compacted and 20% of that amount after being compacted. How much space do all the cans take up after being compacted?"""
    # Define the number of cans and the space taken up by each can
    NUM_CANS = 60
    UNCOMPACTED_SPACE = 30

    # Calculate the space taken up by all the cans before being compacted
    total_uncompacted_space = NUM_CANS * UNCOMPACTED_SPACE

    # Calculate the space taken up by all the cans after being compacted
    COMPACTED_SPACE_MULTIPLIER = 0.2
    compacted_space = total_uncompacted_space * COMPACTED_SPACE_MULTIPLIER

    # Display the space taken up by all the cans after being compacted
    result = compacted_space
    return result

print(solution())