def solution():
    """Alex has 2 cakes that are each cut into 8 slices. A fourth of the slices are given away to his friends. A third of the remaining slices are given away to his family. Alex eats 3 slices. How many slices of the cake are left?"""
    total_slices = 2 * 8
    friend_slices = total_slices // 4
    remaining_slices = total_slices - friend_slices
    family_slices = remaining_slices // 3
    remaining_slices -= family_slices
    remaining_slices -= 3 # Alex eats 3 slices
    result = remaining_slices
    return result

print(solution())