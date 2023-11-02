def solution():
    """Alice is planting bushes around three sides of her yard. If each side is 16 feet long, and each bush fills 4 feet, how many bushes does she need to buy?"""
    # Define the length of each side of Alice's yard
    side_length = 16

    # Calculate the total perimeter of the three sides
    perimeter = side_length * 3

    # Calculate the number of bushes needed
    bushes_needed = perimeter / 4

    # Display the number of bushes needed
    result = bushes_needed
    return result

print(solution())