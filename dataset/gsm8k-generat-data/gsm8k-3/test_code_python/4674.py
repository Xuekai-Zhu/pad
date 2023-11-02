def solution():
    """Steve is 5'6".  He grows 6 inches.  How tall is he in inches?"""
    # Convert Steve's height from feet and inches to just inches
    current_height = 5*12 + 6
    # Add the 6 inches that he grew
    new_height = current_height + 6

    # Display Steve's new height in inches
    result = new_height
    return result

print(solution())