def solution():
    """Greg is riding his bike around town and notices that each block he rides, his wheels rotate 200 times. He's now on a a trail and wants to make sure he rides at least 8 blocks. His wheels have already rotated 600 times, how many more times do they need to rotate to reach his goal?"""
    # Define the number of blocks he wants to ride
    blocks_goal = 8

    # Define the number of wheel rotations per block
    rotations_per_block = 200

    # Define the number of wheel rotations he has already completed
    rotations_completed = 600

    # Calculate the total number of wheel rotations needed to reach his goal
    rotations_needed = (blocks_goal * rotations_per_block) - rotations_completed

    # Return the result
    result = rotations_needed
    return result

print(solution())