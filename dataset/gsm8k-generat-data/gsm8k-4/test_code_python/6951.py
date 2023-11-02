def solution():
    """Bubba bought a new two-story warehouse. When empty, the first floor of the building contains twice as much floor space for storage as the second floor. The first items he brought into his empty building were several thousand boxes; and he put them all on the second floor, which filled one-quarter of the second floor storage space. If the boxes used up 5,000 square feet of storage space, how many square feet of storage space is still available in the building?"""
    # Define the ratio of storage space on the first and second floors
    first_floor_ratio = 2
    second_floor_ratio = 1

    # Calculate the total storage space on both floors
    total_space = 5000 / 0.25

    # Calculate the storage space on the second floor
    second_floor_space = total_space / (second_floor_ratio + first_floor_ratio)

    # Calculate the storage space on the first floor
    first_floor_space = second_floor_space * first_floor_ratio

    # Calculate the remaining storage space
    remaining_space = total_space - (first_floor_space + second_floor_space)

    result = remaining_space
    return result

print(solution())