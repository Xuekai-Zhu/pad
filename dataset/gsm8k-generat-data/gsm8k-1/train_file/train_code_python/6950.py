def solution():
    """Bubba bought a new two-story warehouse. When empty, the first floor of the building contains twice as much floor space for storage as the second floor. The first items he brought into his empty building were several thousand boxes; and he put them all on the second floor, which filled one-quarter of the second floor storage space. If the boxes used up 5,000 square feet of storage space, how many square feet of storage space is still available in the building?"""
    second_floor_space = 5000 / 0.25
    first_floor_space = 2 * second_floor_space
    total_space = first_floor_space + second_floor_space
    available_space = total_space - 5000
    result = available_space
    return result

print(solution())