def solution():
    """Tamia is making dinner. She is using 5 bell peppers to make her meal. She likes to have a variety of sizes so some will melt and some will be thick enough to eat whole. First she cuts each bell pepper into 20 large slices. Then she takes half those slices and cuts them into 3 smaller pieces each. How many slices and pieces of bell pepper total is Tamia going to add to her meal?"""
    bell_peppers = 5
    large_slices_per_pepper = 20
    
    total_large_slices = bell_peppers * large_slices_per_pepper
    small_slices_per_large_slice = 3

    small_slices = (total_large_slices / 2) * small_slices_per_large_slice
    
    total_slices = total_large_slices + small_slices
    result = total_slices
    return result

print(solution())