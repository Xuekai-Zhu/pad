def solution():
    """Jill likes to watch shows on her favorite streaming service. She watched a show that was 30 minutes long, and then watched another show that was 4 times longer. How many total minutes did she spend watching shows?"""
    # Define the length of the first show in minutes
    show1_length = 30

    # Define the length of the second show in terms of the first show's length
    show2_length = 4 * show1_length

    # Calculate the total length of the two shows
    total_length = show1_length + show2_length

    # Display the total length in minutes
    result = total_length
    return result

print(solution())