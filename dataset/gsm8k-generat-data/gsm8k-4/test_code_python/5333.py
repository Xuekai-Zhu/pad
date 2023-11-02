def solution():
    """Tamia is making dinner. She is using 5 bell peppers to make her meal. She likes to have a variety of sizes so some will melt and some will be thick enough to eat whole. First she cuts each bell pepper into 20 large slices. Then she takes half those slices and cuts them into 3 smaller pieces each. How many slices and pieces of bell pepper total is Tamia going to add to her meal?"""
    
    # Define the number of bell peppers and the number of slices per bell pepper
    bell_peppers = 5
    large_slices = 20
    
    # Calculate the total number of large slices
    total_large_slices = bell_peppers * large_slices
    
    # Calculate the number of large slices that will be cut into smaller pieces
    small_slices = total_large_slices // 2
    
    # Calculate the total number of smaller pieces
    total_small_pieces = small_slices * 3
    
    # Calculate the total number of slices and pieces
    total_slices_and_pieces = total_large_slices + total_small_pieces
    
    result = total_slices_and_pieces
    return result

print(solution())