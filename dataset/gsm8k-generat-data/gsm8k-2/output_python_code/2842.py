def solution():
    """Greg is riding his bike around town and notices that each block he rides, his wheels rotate 200 times. He's now on a a trail and wants to make sure he rides at least 8 blocks. His wheels have already rotated 600 times, how many more times do they need to rotate to reach his goal?"""
    rotations_per_block = 200
    blocks_to_ride = 8
    starting_rotations = 600
    total_rotations_needed = (blocks_to_ride * rotations_per_block) - starting_rotations
    result = total_rotations_needed
    return result

print(solution())