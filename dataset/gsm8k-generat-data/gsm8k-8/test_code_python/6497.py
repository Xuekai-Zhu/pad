def solution():
    # Define the initial ratio of marbles between Mario and Manny
    mario_to_manny_ratio = 4/5

    # Calculate the total number of marbles
    total_marbles = 36

    # Calculate the number of marbles that Manny has initially
    manny_initial = total_marbles * (5/9)

    # Manny gives 2 marbles to his brother
    manny_after_giving = manny_initial - 2
    result = manny_after_giving
    return result

print(solution())