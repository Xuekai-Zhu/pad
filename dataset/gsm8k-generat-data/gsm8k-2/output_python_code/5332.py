def solution():
    """Tamia is making dinner. She is using 5 bell peppers to make her meal. She likes to have a variety of sizes so some will melt and some will be thick enough to eat whole. First she cuts each bell pepper into 20 large slices. Then she takes half those slices and cuts them into 3 smaller pieces each. How many slices and pieces of bell pepper total is Tamia going to add to her meal?"""
    bell_peppers = 5
    large_slices_per_bell_pepper = 20
    small_pieces_per_large_slice = 3
    total_slices = bell_peppers * large_slices_per_bell_pepper
    total_small_pieces = (total_slices / 2) * small_pieces_per_large_slice
    total_bell_pepper_parts = total_slices + total_small_pieces
    result = total_bell_pepper_parts
    return result

print(solution())