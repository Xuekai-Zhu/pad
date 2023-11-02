def solution():
    """48 children are trying to share a pack of sweets. After taking 4 sweets each, there is still a third of the original amount left. What is the original number of sweets in the pack?"""
    # Define the number of children and sweets taken by each child
    num_children = 48
    sweets_per_child = 4

    # Calculate the total number of sweets taken
    total_sweets_taken = num_children * sweets_per_child

    # Calculate the remaining sweets
    remaining_sweets = total_sweets_taken / (1/3)

    # Calculate the original number of sweets
    original_sweets = remaining_sweets + total_sweets_taken

    # return the result
    result = original_sweets
    return result

print(solution())