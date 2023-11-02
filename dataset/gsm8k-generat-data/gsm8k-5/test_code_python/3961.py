def solution():
    north_blocks = 3
    west_blocks = 7*north_blocks
    south_blocks = 8
    east_blocks = 2*south_blocks
    total_blocks = west_blocks + east_blocks
    minutes_to_home = total_blocks / 2 # walking rate of 2 blocks/minute
    result = minutes_to_home
    return result

print(solution())