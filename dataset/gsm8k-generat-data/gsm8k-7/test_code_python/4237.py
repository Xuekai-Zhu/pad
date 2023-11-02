def solution():
    total_length = 74.5
    part1_length = 15.5
    part2_length = 21.5
    part3_length = 21.5

    # Calculate the total length of the first three parts of the race
    first_three_parts_length = part1_length + (2 * part2_length)

    # Calculate the length of the fourth and final part of the race
    fourth_part_length = total_length - first_three_parts_length
    result = fourth_part_length
    return result

print(solution())