def solution():
    """Alice is planting bushes around three sides of her yard. If each side is 16 feet long, and each bush fills 4 feet, how many bushes does she need to buy?"""
    # Define the length of each side and the size of each bush
    side_length = 16
    bush_size = 4

    # Calculate the perimeter of three sides
    perimeter = 3 * side_length

    # Calculate the number of bushes needed to fill the perimeter
    bushes_needed = perimeter / bush_size

    # Round up the number of bushes to the nearest whole number
    bushes_needed = int(bushes_needed + 0.5)

    # Return the result
    result = bushes_needed
    return result

print(solution())