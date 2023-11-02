def solution():
    """A 10 meters yarn was cut into 5 equal parts. If 3 parts were used for crocheting, how long was used for crocheting?"""
    # Define the length of the yarn
    yarn_length = 10

    # Divide the yarn length into 5 equal parts
    part_length = yarn_length / 5

    # Calculate the length used for crocheting
    crocheting_length = part_length * 3

    # Display the length used for crocheting
    result = crocheting_length
    return result

print(solution())