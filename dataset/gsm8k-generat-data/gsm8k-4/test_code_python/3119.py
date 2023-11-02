def solution():
    """Nick has 60 cans. Each can takes up 30 square inches of space before being compacted and 20% of that amount after being compacted. How much space do all the cans take up after being compacted?"""
    # Define the number of cans and the space each can takes up before and after being compacted
    num_cans = 60
    space_per_can_before = 30
    space_per_can_after = space_per_can_before * 0.2

    # Calculate the total space taken up by all the cans before and after being compacted
    total_space_before = num_cans * space_per_can_before
    total_space_after = num_cans * space_per_can_after

    # Return the space taken up after being compacted
    result = total_space_after
    return result

print(solution())