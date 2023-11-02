def solution():
    """Tamia is making dinner. She is using 5 bell peppers to make her meal. She likes to have a variety of sizes so some will melt and some will be thick enough to eat whole. First, she cuts each bell pepper into 20 large slices. Then she takes half those slices and cuts them into 3 smaller pieces each. How many slices and pieces of bell pepper total is Tamia going to add to her meal?"""
    # Define the number of bell peppers used
    bell_pepper_count = 5

    # Calculate the total number of slices
    large_slices = bell_pepper_count * 20
    small_slices = (large_slices // 2) * 3
    total_slices = large_slices + small_slices

    # Display the total number of slices and pieces
    result = total_slices
    return result

print(solution())