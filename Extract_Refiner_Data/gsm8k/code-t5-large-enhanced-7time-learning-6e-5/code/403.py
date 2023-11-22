def solution():
    
    # Define the total number of steps
    total_steps = 10000

    # Calculate the number of steps finished on walks
    walk_steps = total_steps / 2

    # Calculate the number of steps taken during the walk
    walk_steps = walk_steps - 1000

    # Calculate the number of steps taken during the short jog
    jog_steps = walk_steps + 1000 - 2000

    # Display the number of steps taken during the jog
    result = jog_steps
    return result

print(solution())