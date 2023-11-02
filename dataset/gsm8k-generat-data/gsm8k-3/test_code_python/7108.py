def solution():
    """As a child, Bobby was able to jump rope 30 times per minute. Now that he is an adult, he can jump 1 jump per second. How many more jumps than when he was a child is Bobby able to jump now that he is an adult?"""
    # Define the number of jumps per minute as a child
    CHILD_JUMPS_PER_MINUTE = 30

    # Define the number of jumps per second as an adult
    ADULT_JUMPS_PER_SECOND = 1

    # Calculate the total number of jumps as a child
    total_child_jumps = CHILD_JUMPS_PER_MINUTE * 60

    # Calculate the total number of jumps as an adult
    total_adult_jumps = ADULT_JUMPS_PER_SECOND * 60 * 60

    # Calculate the difference in jumps
    jump_difference = total_adult_jumps - total_child_jumps

    # Display the difference in jumps
    result = jump_difference
    return result

print(solution())