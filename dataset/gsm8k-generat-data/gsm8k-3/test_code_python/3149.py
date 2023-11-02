def solution():
    """Isaac cut his 30 meters ribbon into 6 equal parts. He then used 4 parts of the ribbon. How many meters of ribbon are not used?"""
    # Define the length of the ribbon and the number of parts it is cut into
    ribbon_length = 30
    num_parts = 6

    # Calculate the length of one part of the ribbon
    part_length = ribbon_length / num_parts

    # Calculate the length of the ribbon that Isaac used
    used_length = 4 * part_length

    # Calculate the length of the ribbon that is not used
    unused_length = ribbon_length - used_length

    # Display the length of the ribbon that is not used
    result = unused_length
    return result

print(solution())