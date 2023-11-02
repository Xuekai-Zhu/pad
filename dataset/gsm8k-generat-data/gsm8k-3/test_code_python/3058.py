def solution():
    """Barkley gets 10 new dog bones at the beginning of the month.  After 5 months, he has 8 bones available and has buried the rest.  How many bones has he buried?"""
    # Define the number of bones Barkley starts with and the number of bones he has left after 5 months
    initial_bones = 10
    bones_left = 8

    # Calculate the number of bones Barkley has buried
    bones_buried = initial_bones * 5 - bones_left

    # Display the number of bones Barkley has buried
    result = bones_buried
    return result

print(solution())