def solution():
    total_length = 30  # Isaac's ribbon is 30 meters long
    parts = 6  # He cuts the ribbon into 6 equal parts
    used_parts = 4  # He uses 4 parts of the ribbon

    # Calculate the length of each part
    part_length = total_length / parts

    # Calculate the length of the parts that he used
    used_length = used_parts * part_length

    # Calculate the length of the parts that he did not use
    unused_length = total_length - used_length
    result = unused_length
    return result

print(solution())