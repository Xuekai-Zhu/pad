def solution():
    """James was 2/3s as tall as his uncle who is 72 inches. He gets a growth spurt that makes him gain 10 inches.  How much taller is his uncle than James now?"""
    # Define the uncle's height
    uncle_height = 72

    # Calculate James's original height
    james_height = 2/3 * uncle_height

    # Calculate James's new height after the growth spurt
    james_new_height = james_height + 10

    # Calculate the difference in height between James and his uncle
    height_difference = uncle_height - james_new_height

    # Display the height difference
    result = height_difference
    return result

print(solution())