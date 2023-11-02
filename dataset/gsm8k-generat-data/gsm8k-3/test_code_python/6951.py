def solution():
    """Bubba bought a new two-story warehouse.  When empty, the first floor of the building contains twice as much floor space for storage as the second floor.  The first items he brought into his empty building were several thousand boxes; and he put them all on the second floor, which filled one-quarter of the second floor storage space.  If the boxes used up 5,000 square feet of storage space, how many square feet of storage space is still available in the building?"""
    # Define the ratio of first floor to second floor storage space
    FLOOR_RATIO = 2

    # Calculate the total storage space available in the building
    second_floor_space = 5000 / 0.25  # Calculate the total second floor storage space
    first_floor_space = FLOOR_RATIO * second_floor_space  # Calculate the total first floor storage space
    total_space = first_floor_space + second_floor_space

    # Calculate the used storage space in the building
    used_space = 5000

    # Calculate the remaining storage space in the building
    remaining_space = total_space - used_space

    # Display the remaining storage space
    result = remaining_space
    return result

print(solution())