def solution():
    # Calculate the number of stone blocks filled by Stella and Twinkle in 4 hours
    stella_twinkle_blocks = 2 * 250 * 4  # 2 people filling up 250 blocks per hour for 4 hours

    # Calculate the number of stone blocks filled by 6 people who joined after 4 hours
    joined_people_blocks = 6 * 250 * x  # 6 people filling up 250 blocks per hour for x hours

    # Find the value of x (number of hours) when the total number of blocks filled is 6000
    total_blocks_filled = stella_twinkle_blocks + joined_people_blocks
    x = (6000 - stella_twinkle_blocks) / (6 * 250)

    # Add the initial 4 hours to get the total time taken to fill the truck
    time_taken = 4 + x
    result = time_taken
    return result

print(solution())