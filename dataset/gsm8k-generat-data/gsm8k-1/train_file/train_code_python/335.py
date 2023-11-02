def solution():
    """Alex has 2 cakes that are each cut into 8 slices. A fourth of the slices are given away to his friends. A third of the remaining slices are given away to his family. Alex eats 3 slices. How many slices of the cake are left?"""
    num_cakes = 2
    cake_slices = 8
    slices_given_away = (num_cakes * cake_slices) // 4
    slices_remaining = (num_cakes * cake_slices) - slices_given_away
    slices_given_to_family = slices_remaining // 3
    slices_remaining -= slices_given_to_family
    slices_remaining -= 3  # slices Alex eats
    result = slices_remaining
    return result

print(solution())