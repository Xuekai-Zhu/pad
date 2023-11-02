def solution():
    """Bubba bought a new two-story warehouse. When empty, the first floor of the building contains twice as much floor space for storage as the second floor. The first items he brought into his empty building were several thousand boxes; and he put them all on the second floor, which filled one-quarter of the second floor storage space. If the boxes used up 5,000 square feet of storage space, how many square feet of storage space is still available in the building?"""
    second_floor_space = 5000 * 4
    first_floor_space = second_floor_space * 2
    total_space = first_floor_space + second_floor_space
    remaining_space = total_space - (5000 + second_floor_space)
    result = remaining_space
    return result

print(solution())