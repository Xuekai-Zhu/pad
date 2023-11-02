def solution():
    """If Mr. Jones has 6 shirts for every pair of pants, and he has 40 pants, what's the total number of pieces of clothes he owns if all other factors remain the same?"""
    # Define the ratio of shirts to pants
    shirts_to_pants = 6

    # Calculate the number of shirts Mr. Jones has
    num_shirts = shirts_to_pants * 40

    # Calculate the total number of pieces of clothes Mr. Jones owns
    total_pieces = num_shirts + 40

    # Return the result
    result = total_pieces
    return result

print(solution())