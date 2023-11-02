def solution():
    """Phil and Andre decide to order some pizza. They get a small cheese and a large pepperoni. The small pizza has 8 slices,
    The large has 14 slices. They have both eaten 9 slices already. How many pieces are left per person?"""
    small_pizza_slices = 8
    large_pizza_slices = 14
    total_slices = small_pizza_slices + large_pizza_slices
    eaten_slices = 9 + 9
    remaining_slices = total_slices - eaten_slices
    slices_per_person = remaining_slices / 2
    result = slices_per_person
    return result

print(solution())