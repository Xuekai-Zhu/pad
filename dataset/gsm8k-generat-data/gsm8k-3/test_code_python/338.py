def solution():
    """Alex has 2 cakes that are each cut into 8 slices. A fourth of the slices are given away to his friends. A third of the remaining slices are given away to his family. Alex eats 3 slices. How many slices of the cake are left?"""
    # Define the number of cakes and slices per cake
    CAKES = 2
    SLICES_PER_CAKE = 8

    # Calculate the total number of slices
    total_slices = CAKES * SLICES_PER_CAKE

    # Calculate the number of slices given away to friends
    slices_to_friends = total_slices // 4

    # Calculate the number of slices remaining
    slices_remaining = total_slices - slices_to_friends

    # Calculate the number of slices given away to family
    slices_to_family = slices_remaining // 3

    # Calculate the number of slices remaining after Alex eats 3
    slices_left = slices_remaining - slices_to_family - 3

    # Display the number of slices left
    result = slices_left
    return result

print(solution())