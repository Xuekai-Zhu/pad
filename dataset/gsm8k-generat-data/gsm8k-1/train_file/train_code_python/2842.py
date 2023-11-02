def solution():
    """Greg is riding his bike around town and notices that each block he rides, his wheels rotate 200 times. He's now on a trail and wants to make sure he rides at least 8 blocks. His wheels have already rotated 600 times, how many more times do they need to rotate to reach his goal?"""
    blocks_to_ride = 8
    rotations_per_block = 200
    starting_rotations = 600
    total_rotations_needed = blocks_to_ride * rotations_per_block
    rotations_remaining = total_rotations_needed - starting_rotations
    result = rotations_remaining
    return result

print(solution())