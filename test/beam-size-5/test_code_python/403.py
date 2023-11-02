def solution():
    
    # Define the total number of steps Elliott walks in a day
    total_steps = 10000 * 7

    # Calculate the number of steps Elliott finished on his walks to and from school
    walks_to_school = total_steps / 2

    # Calculate the number of steps Elliott finished on his short walk
    short_walks = 1000

    # Calculate the number of steps Elliott finished on his jog
    jog_steps = total_steps - walks_to_school - short_walks

    # Calculate the number of steps Elliott took during his jog
    jog_steps = jog_steps

    # Display the number of steps Elliott took during his jog
    result = jog_steps
    return result

print(solution())