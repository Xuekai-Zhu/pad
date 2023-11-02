def solution():
    """Greg is riding his bike around town and notices that each block he rides, his wheels rotate 200 times. He's now on a a trail and wants to make sure he rides at least 8 blocks. His wheels have already rotated 600 times, how many more times do they need to rotate to reach his goal?"""
    # Define the number of blocks Greg wants to ride
    blocks = 8

    # Define the number of wheel rotations per block
    rotations_per_block = 200

    # Define the current number of wheel rotations
    current_rotations = 600

    # Calculate the total number of wheel rotations Greg needs to reach his goal
    total_rotations_needed = blocks * rotations_per_block

    # Calculate the number of additional wheel rotations Greg needs to reach his goal
    additional_rotations_needed = total_rotations_needed - current_rotations

    # Display the number of additional wheel rotations needed
    result = additional_rotations_needed
    return result

print(solution())