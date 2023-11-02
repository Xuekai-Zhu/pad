def solution():
    """A YouTube video got 3000 likes and 100 more than half as many dislikes. If the video gets 1000 more dislikes and 0 more likes how many dislikes does the video have?"""
    # Calculate the initial number of dislikes
    dislikes_initial = (3000 - 100) * 2

    # Add the additional dislikes
    dislikes_final = dislikes_initial + 1000

    # Return the final number of dislikes
    result = dislikes_final
    return result

print(solution())