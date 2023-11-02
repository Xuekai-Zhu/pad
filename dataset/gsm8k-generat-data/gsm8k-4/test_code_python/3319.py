def solution():
    """A 10 meters yarn was cut into 5 equal parts. If 3 parts were used for crocheting, how long was used for crocheting?"""
    # Define the total length of the yarn and the number of parts
    total_length = 10
    num_parts = 5

    # Calculate the length of each part
    part_length = total_length / num_parts

    # Calculate the length of the yarn used for crocheting
    crochet_length = part_length * 3

    # return the result
    result = crochet_length
    return result

print(solution())