def solution():
    # Calculate the total number of blocks Janet walks
    blocks_walked = 3 + 7*3 + 8 + 2*21  # Janet walks 3 blocks north, then 21 blocks west (7 times 3), then 8 blocks south, and finally 42 blocks east (twice 21)

    # Calculate the time it will take Janet to walk home
    time_taken = blocks_walked / 2  # Janet walks at a speed of 2 blocks/minute

    result = time_taken
    return result

print(solution())