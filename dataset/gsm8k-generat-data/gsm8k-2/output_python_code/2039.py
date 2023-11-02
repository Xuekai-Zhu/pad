def solution():
    """Phil and Andre decide to order some pizza. They get a small cheese and a large pepperoni. The small pizza has 8 slices, The large has 14 slices. They have both eaten 9 slices already. How many pieces are left per person?"""
    total_slices = 8 + 14
    eaten_slices = 9 + 9
    remaining_slices = total_slices - eaten_slices
    slices_per_person = remaining_slices / 2
    result = slices_per_person
    return result

print(solution())