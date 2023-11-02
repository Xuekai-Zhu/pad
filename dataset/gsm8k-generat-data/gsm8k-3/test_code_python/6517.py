def solution():
    """Mabel lives 4500 steps directly east of Lake High school. Helen lives 3/4 the number of steps that Mabel lives, directly west of the school. What's the total number of steps Mabel will walk to visit Helen so that they can do their assignments together?"""
    # Define the number of steps Mabel lives from the school
    mabel_steps = 4500

    # Define the number of steps Helen lives from the school
    helen_steps = mabel_steps * (3/4)

    # Calculate the total number of steps Mabel will walk to visit Helen
    total_steps = mabel_steps + helen_steps

    # Display the total number of steps
    result = total_steps
    return result

print(solution())