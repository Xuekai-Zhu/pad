def solution():
    """Isaac cut his 30 meters ribbon into 6 equal parts. He then used 4 parts of the ribbon. How many meters of ribbon are not used?"""
    # Define the length of the ribbon and the number of equal parts
    ribbon_length = 30
    num_parts = 6

    # Calculate the length of each part
    part_length = ribbon_length / num_parts

    # Calculate the length of the ribbon used
    used_length = part_length * 4

    # Calculate the length of the ribbon not used
    not_used_length = ribbon_length - used_length

    # return the result
    result = not_used_length
    return result

print(solution())